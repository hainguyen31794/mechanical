# Dự án tạo hình tròn chuyển động có quỹ đạo
import tkinter as tk
import math
from queue import Queue
# Tạo lớp hình tròn
arrCircle = []
rootNode = None
class Circle():
	"""docstring for Circle"""
	# Khởi tạo hình tròn
	def __init__(self, center, radius): # center là 1 mảng tọa độ (x, y)
		self.center = center # Tọa độ tâm O
		self.radius = radius # Bán kính
		self.connect = []
		self._config_circle = None
		arrCircle.append(self)
		self.__connect_other()

	# Kiểm tra tiếp xúc giữa 2 hình tròn
	def __tangent(self, other):
		distance = math.sqrt((self.center[0] - other.center[0])**2 + (self.center[1] - other.center[1])**2)
		if self.radius + other.radius == distance:
			return 1 # Tiếp xúc
		elif (self.radius + other.radius > distance) or distance < (max(self.radius, other.radius)):
			return -1 # Giao nhau
		else:
			return 0 # Không giao nhau
	def __connect_other(self):
		for other in arrCircle[:-1:]: 
			_tangent = self.__tangent(other)
			if (_tangent == -1):
				arrCircle.pop()
				break
			elif (_tangent == 1):
				self.connect.append(other)
				other.connect.append(self)

	@property
	def config_circle(self):
		return self._config_circle
	@config_circle.setter
	def config_circle(self, value):
		if value[0]>0 and value[1] != None:
			self._config_circle = value
			global rootNode
			rootNode = self

visited = [False for i in range(50)]			
graph = [[] for i in range(50)]


def BFS(root):
	q = Queue()
	visited[root] = True
	q.put(root)
	while q.empty() == False:
		u = q.get()
		obj = hash_circle[u]
		
		for v in graph[u]:
			if visited[v] == False:
				hash_circle[v].config_circle = (obj.radius*obj.config_circle[0]/ hash_circle[v].radius, not obj.config_circle[1] )
				visited[v] = True
				q.put(v)

hinhtron0 = Circle((0, 0), 1)  #0
hinhtron2 = Circle((8,0), 2) #1
hinhtron4 = Circle((16, 0), 4)#2
hinhtron1 = Circle((3.5, 0), 2.5)#3
hinhtron3 = Circle((11, 0), 1)#4


hinhtron4.config_circle = (23, True)

hash_circle = {}
for i, other in enumerate(arrCircle):
	hash_circle[i] = other
rev = {v: k for k,v in hash_circle.items()}

for other in arrCircle:
	graph[rev[other]] =[rev[i] for i in other.connect]
BFS(2)

print(hinhtron2.config_circle)