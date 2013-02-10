o, b, y, w, g, r = 'orange', 'blue', 'yellow', 'white', 'green', 'red'

class Cube():

	def __init__(self, faces):
		self.faces = faces
		self.f = faces[1]
		self.b = faces[4]
		self.d = faces[3]
		self.t = faces[5]
		self.l = faces[0]
		self.r = faces[2]

	def copy(self):
		return Cube([self.l[:], self.f[:], self.r[:], self.d[:], self.b[:], self.t[:]])

	def isGoalState(self):
		for face in self.faces:
			color = face[4]
			for grid in face:
				if grid != color:
					return False
		return True

	def clockwise(self, f):
		return [f[6], f[3], f[0], f[7], f[4], f[1], f[8], f[5], f[2]]

	def counterClockwise(self, f):
		return [f[2], f[5], f[8], f[1], f[4], f[7], f[0], f[3], f[6]]

	def left(self):
		self.l = self.clockwise(self.l)
		for i in (0, 3, 6):
			self.f[i], self.d[i], self.b[i], self.t[i] = self.t[i], self.f[i], self.d[i], self.b[i]

	def counterLeft(self):
		self.l = self.counterClockwise(self.l)
		for i in (0, 3, 6):
			self.f[i], self.d[i], self.b[i], self.t[i] = self.d[i], self.b[i], self.t[i], self.f[i]

	def right(self):
		self.r = self.clockwise(self.r)
		for i in (2, 5, 8):
			self.f[i], self.d[i], self.b[i], self.t[i] = self.d[i], self.b[i], self.t[i], self.f[i]

	def counterRight(self):
		self.r = self.counterClockwise(self.r)
		for i in (2, 5, 8):
			self.f[i], self.d[i], self.b[i], self.t[i] = self.t[i], self.f[i], self.d[i], self.b[i]

	def front(self):
		self.f = self.clockwise(self.f)
		self.l[8], self.t[6], self.r[0], self.d[2] = self.d[2], self.l[8], self.t[6], self.r[0]
		self.l[5], self.t[7], self.r[3], self.d[1] = self.d[1], self.l[5], self.t[7], self.r[3]
		self.l[2], self.t[8], self.r[6], self.d[0] = self.d[0], self.l[2], self.t[8], self.r[6]

	def counterFront(self):
		self.f = self.counterClockwise(self.f)
		self.l[8], self.t[6], self.r[0], self.d[2] = self.t[6], self.r[0], self.d[2], self.l[8]
		self.l[5], self.t[7], self.r[3], self.d[1] = self.t[7], self.r[3], self.d[1], self.l[5]
		self.l[2], self.t[8], self.r[6], self.d[0] = self.t[8], self.r[6], self.d[0], self.l[2]

	def back(self):
		self.b = self.clockwise(self.b)
		self.l[6], self.t[2], self.r[8], self.d[6] = self.t[2], self.r[8], self.d[6], self.l[6]
		self.l[3], self.t[1], self.r[5], self.d[7] = self.t[1], self.r[5], self.d[7], self.l[3]
		self.l[0], self.t[0], self.r[2], self.d[8] = self.t[0], self.r[2], self.d[8], self.l[0]

	def counterBack(self):
		self.b = self.counterClockwise(self.b)
		self.l[6], self.t[2], self.r[8], self.d[6] = self.d[6], self.l[6], self.t[2], self.r[8]
		self.l[3], self.t[1], self.r[5], self.d[7] = self.d[7], self.l[3], self.t[1], self.r[5]
		self.l[0], self.t[0], self.r[2], self.d[8] = self.d[8], self.l[0], self.t[0], self.r[2]

	def top(self):
		self.t = self.clockwise(self.t)
		self.l[2], self.b[6], self.r[2], self.f[2] = self.f[2], self.l[2], self.b[6], self.r[2]
		self.l[1], self.b[7], self.r[1], self.f[1] = self.f[1], self.l[1], self.b[7], self.r[1]
		self.l[0], self.b[8], self.r[0], self.f[0] = self.f[0], self.l[0], self.b[8], self.r[0]

	def counterTop(self):
		self.t = self.counterClockwise(self.t)
		self.l[2], self.b[6], self.r[2], self.f[2] = self.b[6], self.r[2], self.f[2], self.l[2]
		self.l[1], self.b[7], self.r[1], self.f[1] = self.b[7], self.r[1], self.f[1], self.l[1]
		self.l[0], self.b[8], self.r[0], self.f[0] = self.b[8], self.r[0], self.f[0], self.l[0]

	def bot(self):
		self.d = self.clockwise(self.d)
		self.l[6], self.b[2], self.r[6], self.f[6] = self.b[2], self.r[6], self.f[6], self.l[6]
		self.l[7], self.b[1], self.r[7], self.f[7] = self.b[1], self.r[7], self.f[7], self.l[7]
		self.l[8], self.b[0], self.r[8], self.f[8] = self.b[0], self.r[8], self.f[8], self.l[8]

	def counterBot(self):
		self.d = self.counterClockwise(self.d)
		self.l[6], self.b[2], self.r[6], self.f[6] = self.f[6], self.l[6], self.b[2], self.r[6]
		self.l[7], self.b[1], self.r[7], self.f[7] = self.f[7], self.l[7], self.b[1], self.r[7]
		self.l[8], self.b[0], self.r[8], self.f[8] = self.f[8], self.l[8], self.b[0], self.r[8]

	def switchFace(self, side):
		if side == 3:
			self.f, self.d, self.b, self.t = self.d, self.b, self.t, self.f
			self.l, self.r = self.counterClockwise(self.l), self.clockwise(self.r)
		elif side == 4:
			self.f, self.d, self.b, self.t = self.b, self.t, self.f, self.d
			self.l, self.r = self.counterClockwise(self.l), self.clockwise(self.r)
			self.l, self.r = self.counterClockwise(self.l), self.clockwise(self.r)
		elif side == 5:
			self.f, self.d, self.b, self.t = self.t, self.f, self.d, self.b
			self.l, self.r = self.clockwise(self.l), self.counterClockwise(self.r)
		elif side == 0:
			self.b, self.r = self.counterClockwise(self.b), self.counterClockwise(self.r)
			self.b, self.r = self.counterClockwise(self.b), self.counterClockwise(self.r)
			side.d, side.t = self.clockwise(self.d), self.counterClockwise(self.t)
			self.l, self.r, self.f, self.b = self.f, self.b, self.r, self.l
		elif side == 2:
			self.b, self.r = self.counterClockwise(self.b), self.counterClockwise(self.r)
			self.b, self.r = self.counterClockwise(self.b), self.counterClockwise(self.r)
			side.d, side.t = self.counterClockwise(self.d), self.clockwise(self.t)
			self.l, self.r, self.f, self.b = self.b, self.f, self.l, self.r

	def moves(self):
		return ('left', 'counterLeft', 'right', 'counterRight', 'front', 'counterFront', 'back', 'counterBack', 'top', 'counterTop', 'bot', 'counterBot')

def solve(cube):
	queue = []
	queue.append((cube, []))
	while len(queue):
		currCube, path = queue.pop(0)
		if currCube.isGoalState():
			return path
		for move in currCube.moves():
			newCube = currCube.copy()
			if move == 'left':
				newCube.left()
			elif move == 'counterLeft':
				newCube.counterLeft()
			elif move == 'right':
				newCube.right()
			elif move == 'counterRight':
				newCube.counterRight()
			elif move == 'front':
				newCube.front()
			elif move == 'counterFront':
				newCube.counterFront()
			elif move == 'back':
				newCube.back()
			elif move == 'counterBack':
				newCube.counterBack()
			elif move == 'top':
				newCube.top()
			elif move == 'counterTop':
				newCube.counterTop()
			elif move == 'bot':
				newCube.bot()
			elif move == 'counterBot':
				newCube.counterBot()
			newPath = path[:]
			newPath.append(move)
			queue.append((newCube, newPath))

def main():
	sides = [
    [y, w, g, g, w, g, g, r, r],
    [r, r, w, r, r, b, b, y, w],
    [b, b, b, y, y, o, b, b, o],
    [y, g, r, y, g, r, o, y, y],
    [w, o, g, w, o, g, g, o, y],
    [r, w, o, b, b, o, w, w, o]
	]

	cube = Cube(sides)
	sol = solve(cube)
	print(1)
	print sol

if __name__ == '__main__':
	main()






