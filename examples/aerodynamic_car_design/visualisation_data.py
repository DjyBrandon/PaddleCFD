# pip install pyvista imageio imageio-ffmpeg
import pyvista as pv
import imageio

mesh = pv.read("./model/quadpress_smpl.vtk")

plotter = pv.Plotter(off_screen=True, window_size=[400, 300])
plotter.add_mesh(mesh, show_edges=True, cmap="jet")

# ---- 设置绕 Y 轴旋转 ----
# 1. 将相机放置在 XZ 平面（高度为0，与Y轴垂直）
# plotter.camera.SetPosition(15, 0, 15)  # 距离原点一定距离
plotter.camera.SetFocalPoint(0, 0, 0)  # 看向原点
plotter.camera.SetViewUp(0, 1, 0)  # 将 Y 轴设为“上方向”
# 这样 Azimuth 旋转将围绕 Y 轴进行

plotter.camera.zoom(2.0)  # 放大2倍
plotter.render()  # 先渲染一帧，确保相机初始化

frames = []
n_frames = 180
angle_step = 2

for _ in range(n_frames):
    plotter.camera.Azimuth(angle_step)
    plotter.render()
    frames.append(plotter.screenshot(return_img=True))

plotter.close()

output_mp4 = "../../tutorials/images/aerodynamic_car_design/rotation_video.mp4"
imageio.mimsave(output_mp4, frames, fps=30)
print(f"视频已生成: {output_mp4}")


output_gif = "../../tutorials/images/aerodynamic_car_design/rotation_video.gif"
imageio.mimsave(output_gif, frames, fps=15)  # GIF 用较低 FPS 文件更小
print(f"GIF 已保存为: {output_gif}")
