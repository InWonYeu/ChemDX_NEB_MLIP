import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["FC"] = "gfortran"


from amp import Amp
from amp.descriptor.gaussian import Gaussian
from amp.model.neuralnetwork import NeuralNetwork
from amp.model import LossFunction
from amp.regression import Regressor


# 1) 모델 생성 (optimizer는 여기서 넘기지 않음)
nn = NeuralNetwork(hiddenlayers=(5, 5))

# 2) Regressor로 옵티마이저 지정 (예: L-BFGS-B, tol 완화)
reg = Regressor(
    optimizer='L-BFGS-B',                 # 또는 'BFGS'
    optimizer_kwargs={
        'options': {
            'gtol': 1e-6,                 # L-BFGS-B/BFGS 모두 options 안에
        }
    },
    lossprime=True                        # gradient 사용
)
nn.regressor = reg

calc = Amp(descriptor=Gaussian(cutoff=4.5),
           model=nn, 
           label='amp', 
           cores=1,
)

calc.model.lossfunction = LossFunction(convergence={'energy_rmse': 0.001},
                                                    energy_coefficient=1.0,
                                                    overfit=0.0001)

calc.train(images='training_set_1.traj', overwrite=True)
