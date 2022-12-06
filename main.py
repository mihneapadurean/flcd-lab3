from fa import FA;

if __name__ == "__main__":
	fa = FA.read_from_file("FA.in")

	print(f"States: {fa.Q}")
	print(f"Alphabet: {fa.E}")
	print(f"Transitions: {fa.d}")
	print(f"Final states: {fa.F}")