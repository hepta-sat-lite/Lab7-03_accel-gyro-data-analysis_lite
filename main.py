import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
filename = ''  #パスを入れる
df = pd.read_csv(filename, header=None, sep=',')

# 列名の設定
df.columns = ['time', 'battery_voltage', 'temperature', 
              'accel_x', 'accel_y', 'accel_z', 
              'gyro_x', 'gyro_y', 'gyro_z', 
              'mag_x', 'mag_y', 'mag_z']

# サブプロット作成
fig, axes = plt.subplots(4, 1, figsize=(12, 20), sharex=False)

# 1. バッテリー電圧 vs 時間
axes[0].scatter(df['time'], df['battery_voltage'], color='orange', s=10)
axes[0].set_title('Battery Voltage vs Time')
axes[0].set_xlabel('Time [s]')
axes[0].set_ylabel('Battery Voltage [V]')
axes[0].grid()

# 2. 温度 vs 時間
axes[1].scatter(df['time'], df['temperature'], color='red', s=10)
axes[1].set_title('Temperature vs Time')
axes[1].set_xlabel('Time [s]')
axes[1].set_ylabel('Temperature [°C]')
axes[1].grid()

# 3. 加速度  vs 時間
axes[2].scatter(df['time'], df['accel_x'], color='blue', s=10)
axes[2].scatter(df['time'], df['accel_y'], color='green', s=10)
axes[2].scatter(df['time'], df['accel_z'], color='purple', s=10)
axes[2].set_title('Acceleration  vs Time')
axes[2].set_xlabel('Time [s]')
axes[2].set_ylabel('Accel X [m/s²]')
axes[2].grid()


# 6. 角速度（X,Y,Z） vs 時間
axes[3].scatter(df['time'], df['gyro_x'], color='cyan', s=10, label='Gyro X')
axes[3].scatter(df['time'], df['gyro_y'], color='magenta', s=10, label='Gyro Y')
axes[3].scatter(df['time'], df['gyro_z'], color='brown', s=10, label='Gyro Z')
axes[3].set_title('Gyro (X,Y,Z) vs Time')
axes[3].set_xlabel('Time [s]')
axes[3].set_ylabel('Gyro [deg/s]')
axes[3].legend()
axes[3].grid()

plt.tight_layout()
plt.show()
