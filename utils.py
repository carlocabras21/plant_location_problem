from setup import *

def get_folders_list():
	cartelle = []
	
	if bilde:
		cartelle.append(['benchmark_data/BildeKrarup/B', 'benchmark_data/BildeKrarup/C', 'benchmark_data/BildeKrarup/Dq/1', 
					'benchmark_data/BildeKrarup/Dq/2', 'benchmark_data/BildeKrarup/Dq/3', 'benchmark_data/BildeKrarup/Dq/4', 
					'benchmark_data/BildeKrarup/Dq/5', 'benchmark_data/BildeKrarup/Dq/6', 'benchmark_data/BildeKrarup/Dq/7', 
					'benchmark_data/BildeKrarup/Dq/8', 'benchmark_data/BildeKrarup/Dq/9', 'benchmark_data/BildeKrarup/Dq/10', 
					'benchmark_data/BildeKrarup/Eq/1', 'benchmark_data/BildeKrarup/Eq/2', 'benchmark_data/BildeKrarup/Eq/3', 
					'benchmark_data/BildeKrarup/Eq/4', 'benchmark_data/BildeKrarup/Eq/5', 'benchmark_data/BildeKrarup/Eq/6', 
					'benchmark_data/BildeKrarup/Eq/7', 'benchmark_data/BildeKrarup/Eq/8', 'benchmark_data/BildeKrarup/Eq/9', 
					'benchmark_data/BildeKrarup/Eq/10'])
	
	if chess:
		cartelle.append(["benchmark_data/Chess"])
		
	if euclid:
		cartelle.append(["benchmark_data/Euclid"])
		
	if fpp11:
		cartelle.append(["benchmark_data/Fpp11"])
		
	if fpp17:
		cartelle.append(["benchmark_data/Fpp17"])
		
	if gapa:
		cartelle.append(["benchmark_data/GapA"])
	
	if gapb:
		cartelle.append(["benchmark_data/GapB"])
	
	return cartelle
	
def get_tests_list():
	tests = []

	if bilde:
		tests.append("bilde")
		
	if chess:
		tests.append("chess")
		
	if euclid:
		tests.append("euclid")
		
	if fpp11:
		tests.append("fpp11")
		
	if fpp17:
		tests.append("fpp17")
		
	if gapa:
		tests.append("gapa")
		
	if gapb:
		tests.append("gapb")
		
	return tests

def get_time_disc(test, i):
	with open("risultati/times_" + test + ".txt", "r") as f:
		return float(f.readlines()[i].split(" ")[-2])
	

def get_time_cont(test, i):
	with open("risultati/times_" + test + "_cont.txt", "r") as f:
		return float(f.readlines()[i].split(" ")[-2])

def stampa_video_file(s, f, f_log, newlines):
	print (s + "\n" * (newlines - 1))
	f.write(s + "\n" * newlines)
	f_log.write(s + "\n" * newlines)