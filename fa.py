class FA:
	def __init__(self, Q, E, q0, F, d):
		self.Q = Q
		self.E = E
		self.q0 = q0
		self.F = F
		self.d = d
		self.validate()


	@staticmethod
	def read_from_file(file_name):
		with open(file_name, "r") as file:
			Q = file.readline().strip().split()
			E = file.readline().strip().split()
			q0 = file.readline().strip()
			F = file.readline().strip().split()

			d = {}
			for line in file:
				line = line.strip().split(',')

				start = line[0]
				transition = line[1]
				end = line[2]

				if (start, transition) in d.keys():
					d[(start, transition)].append(end)
				else:
					d[(start, transition)] = [end]

		return FA(Q, E, q0, F, d)


	def validate(self):

		for element in self.Q:
			if (element.isalpha() == False):
				raise ValueError("Error: invalid set of states!\n")

		for element in self.E:
			if (ord(element)<33 or ord(element)>126):
				raise ValueError("Error: invalid alphabet!\n")

		if (self.q0.isalpha() == False):
				raise ValueError("Error: invalid initial state!\n")

		for element in self.F:
			if (element.isalpha() == False):
				raise ValueError("Error: invalid set of final states!\n")

		for (state, transition) in self.d.keys():
			if (state.isalpha() == False or ord(transition)<33 or ord(transition)>126):
				raise ValueError("Error: invalid transition function!\n")

		for resultingStates in self.d.values():
			for state in resultingStates:
				if (state.isalpha() == False):
					raise ValueError("Error: invalid transition function!\n")

		