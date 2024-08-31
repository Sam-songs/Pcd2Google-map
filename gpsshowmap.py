import rospy
from geometry_msgs.msg import Vector3Stamped
import folium

# 创建一个空的点列表来存储轨迹点
trajectory_points = []

# 初始化计数器
point_counter = 0

def callback(data):
    global point_counter
    point_counter += 1

    # 每间隔20个点记录一次
    if point_counter % 20 == 0:
        x = data.vector.x
        y = data.vector.y
        z = data.vector.z
        point = (x, y, z)
        trajectory_points.append(point)
        rospy.loginfo(f"Recorded point: {point}")

def listener():
    rospy.init_node('trajectory_listener', anonymous=True)
    rospy.Subscriber('/filter/positionlla', Vector3Stamped, callback)
    rospy.spin()

def save_map(points):
    if not points:
        rospy.loginfo("No points to save.")
        return
    
    # 使用第一个点作为地图的初始中心
    map_center = points[0][:2]
    m = folium.Map(location=map_center, zoom_start=15,
                   tiles="https://mt.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                   attr='google卫星影像图',
                   control_scale=True)

    # 只绘制轨迹线
    folium.PolyLine([point[:2] for point in points], color="blue").add_to(m)
    m.save('trajectory_map.html')

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

    if trajectory_points:
        save_map(trajectory_points)
    else:
        rospy.loginfo("No points received.")

