from matplotlib import pyplot as plt  # 可视化相关
import rawpy  # Raw图解析相关
import numpy as np  # 矩阵运算相关
import cv2  # 影像读取相关

# 读取Raw图
img = rawpy.imread("lawson_raw.dng")

# 直接解析
out_pp = img.postprocess(use_camera_wb=True)

# 先进行处理再解析
pixels = img.raw_image_visible.astype('float32')
# lens shading
xs, ys = np.mgrid[:pixels.shape[0], :pixels.shape[1]]
xs = np.float32(xs) - xs.mean()
ys = np.float32(ys) - ys.mean()
rs = (xs ** 2 + ys ** 2) ** 0.5 / xs.shape[0]
shading = 1 + rs ** 2 * 3
# black level
bl = 64
pixels = bl + (pixels - bl) * 3 * shading
img.raw_image_visible[:] = pixels.clip(0, 1023)

# 利用Rawpy进行软解
out = img.postprocess(use_camera_wb=True)

# 读取手机直出图像作为对比
img_phone = cv2.imread("lawson_phone.jpg")
img_phone_rgb = cv2.cvtColor(img_phone, cv2.COLOR_BGR2RGB)

# 可视化
plt.figure(1)
plt.title("postprocess")
plt.imshow(out_pp, cmap='gray')
plt.figure(2)
plt.title("postprocess with lsc")
plt.imshow(out, cmap='gray')
plt.figure(3)
plt.title("phone")
plt.imshow(img_phone_rgb, cmap='gray')
plt.show()
