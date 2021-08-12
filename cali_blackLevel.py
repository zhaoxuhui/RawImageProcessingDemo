from matplotlib import pyplot as plt  # 可视化相关
import rawpy  # Raw图解析相关
import numpy as np

# 读取Raw图
img = rawpy.imread("black_raw.dng")
array_data = img.raw_image_visible

# 遍历像素统计灰度直方图
bins = [0] * 1024
for i in range(array_data.shape[0]):
    print(i + 1, '/', array_data.shape[0])
    for j in range(array_data.shape[1]):
        bins[array_data[i, j]] += 1

for i in range(55, 75):
    print(i, ":", bins[i])

mean_value = np.mean(array_data)
print("Mean value:", mean_value)

# 绘制图像
plt.figure(1)
plt.bar(range(55, 75), bins[55:75])
plt.figure(2)
plt.title("array_data")
plt.imshow(array_data)
plt.show()
