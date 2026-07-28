# MetaX GPU Tutorials


```shell
cd /opt/package/ppcfd/PaddleCFD
```

## 1. Aerodynamic Car Design

> This model can predict drag of the vehicle in different geometry.

![Example](./images/aerodynamic_car_design/example.png)

> [1] Wu H, Luo H, Wang H, et al. Transolver: A fast transformer solver for pdes on general geometries[J]. arXiv preprint arXiv:2402.02366, 2024.

![Original Data](./images/aerodynamic_car_design/rotation_video.gif)

**Configuration:** `MetaX MXC500 64G*1`.

**Speed Up**

| DataSet      | transolver original repo | paddle  |
|--------------|--------------------------|---------|
| ShapeNet-Car | 12 hours                 | 6 hours |
| DrivAerNet++ | TODO                     | TODO    |

**Precision:**

- ShapeNet-Car

| physics | l2 transolver original repo | l2 paddle |
|---------|-----------------------------|-----------|
| surf    | 0.0769                      | 0.0779    |
| volume  | 0.0211                      | 0.0250    |

- DrivAerNet++ (TODO)

**Loss Curve:**

<img src="./images/aerodynamic_car_design/loss_curves.png" style="zoom:20%;" />

### 1.1 Data Download

I downloaded the data to the data disk and linked it to the corresponding data directory.

```shell
# download data (ShapenetCar)
cd /data
wget https://paddle-org.bj.bcebos.com/paddlecfd/datasets/pptransformer/mlcfd_data.zip
unzip mlcfd_data.zip

# create data directory
cd examples/aerodynamic_car_design/
mkdir -p ./data && cd ./data

# create data link
ln -sf /data/training_data /opt/package/ppcfd/PaddleCFD/examples/aerodynamic_car_design/data/training_data
ln -sf /data/preprocessed_data /opt/package/ppcfd/PaddleCFD/examples/aerodynamic_car_design/data/preprocessed_data
ln -sf /data/graph_raw_data /opt/package/ppcfd/PaddleCFD/examples/aerodynamic_car_design/data/graph_raw_data
ln -sf /data/linear_regression_code /opt/package/ppcfd/PaddleCFD/examples/aerodynamic_car_design/data/linear_regression_code
ln -sf /data/side_by_side_comparisons /opt/package/ppcfd/PaddleCFD/examples/aerodynamic_car_design/data/side_by_side_comparisons
```

### 1.2 Checkpoint Download (Optional)

My checkpoint file is located in the `output/Transolver` directory. It was obtained after about 6 hours of training, or you can use the default checkpoint file provided by the official.

```shell
# default ckpt
mkdir -p ./checkpoint/shapenet_car && cd ./checkpoint/shapenet_car
wget https://paddle-org.bj.bcebos.com/paddlecfd/checkpoints/pptransformer/model_131.pdparams
cd .. && cd ..
```

### 1.3 Train (Useless)

The training instructions are as follows. But I have completed the training process. All you need to do is run the test command.

```shell
# ⚠️ You do not need to train
python main_shapenetcar.py
```

### 1.4 Test

You can use either my checkpoint file or the official default checkpoint file for the test.

```shell
# my ckpt
python main_shapenetcar.py mode=test checkpoint=./output/Transolver/20260725_124606/model_199.pdparams

# OR default ckpt
python main_shapenetcar.py mode=test checkpoint=./checkpoint/shapenet_car/model_131.pdparams
```

If test successfully:

![Test 1](./images/aerodynamic_car_design/test_1.png)

![Test 2](./images/aerodynamic_car_design/test_2.png)

## 2. Aerodynamic Airfoil Design


> Given an airfoil’s:
>
> - Geometric parameters (e.g., coordinates, curvature),
> - Flow conditions (e.g., angle of attack, freestream velocity),
>
> PP-DeepOKAN predicts the velocity and pressure distributions over the domain

![Result](../examples/aerodynamics/ppkan/outputs-KANONet/2026-07-28/20-53-56/pressure_pred.png)

**Configuration:** `MetaX MXC500 16G*1`.

**Runtime:** $\approx$ 27 h

**Pressure Field Prediction Metric on the Test Set:** 2.5064e-02

**Loss Curve:**

![Training Curves](../examples/aerodynamics/ppkan/outputs-KANONet/2026-07-26/22-19-54/training_curves.png)

### 2.1 Data Download

I downloaded the data to the data disk and linked it to the corresponding data directory.

```shell
# download data (AirfRANS)
cd /data
wget https://paddle-org.bj.bcebos.com/paddlecfd/datasets/ppkan/AirFoilDataset.zip
unzip AirFoilDataset.zip

# create data link
cd examples/aerodynamics/ppkan
ln -sf /data/Dataset /opt/package/ppcfd/PaddleCFD/examples/aerodynamics/ppkan/Dataset
```

### 2.2 Checkpoint Download (Optional)

My checkpoint file is located in the `outputs-KANONet` directory. It was obtained after about 27 hours of training, or you can use the default checkpoint file provided by the official.

```shell
# default ckpt
mkdir -p ./checkpoint && cd ./checkpoint
wget https://paddle-org.bj.bcebos.com/paddlecfd/checkpoints/ppkan/foil/KANONet_best.pdparams
cd ..
```

### 2.3 Train (Useless)

The training instructions are as follows. But I have completed the training process. All you need to do is run the test command.

```shell
# ⚠️ You do not need to train
python main.py model=KANONet
```

### 2.4 Test

You can use either my checkpoint file or the official default checkpoint file for the test.

```shell
# my ckpt
python main.py mode=test checkpoint=./outputs-KANONet/2026-07-26/22-19-54/KANONet_best.pdparams

# OR default ckpt
python main.py mode=test checkpoint=./checkpoint/KANONet_best.pdparams
```

If test successfully:

![Test 1](./images/aerodynamic_airfoil_design/test_1.png)

![Test 2](./images/aerodynamic_airfoil_design/test_2.png)

## Airfoil Wake Flow

If test successfully:

![]()

## Darcy Flow

If test successfully:

![]()

```shell
```