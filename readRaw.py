from matplotlib import pyplot as plt  # 可视化相关
import rawpy  # Raw图解析相关
import numpy as np  # 矩阵运算相关

# 读取并解析Raw图
img = rawpy.imread("keyboard_raw.dng")
array_data = img.raw_image_visible

# 遍历像素统计灰度直方图
bins = [0] * 1024
for i in range(array_data.shape[0]):
    print(i + 1, '/', array_data.shape[0])
    for j in range(array_data.shape[1]):
        bins[array_data[i, j]] += 1

# 输出相关信息检查灰度统计是否正确
print('Image width:', array_data.shape[0])
print('Image height:', array_data.shape[1])
print('Total pixel:', array_data.shape[0] * array_data.shape[1])
print('Total pixel in practice:', np.sum(bins))
print('Datatype:', array_data.dtype)

# 绘制灰度直方图
plt.figure(1)
plt.bar(range(len(bins)), bins)

# 绘制Raw图
plt.figure(2)
plt.imshow(array_data, cmap='gray')

# 可视化
plt.show()
