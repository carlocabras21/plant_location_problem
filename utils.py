from setup import *

def get_folders_list():
	cartelle = []
	
	if bilde:
		cartelle += ['benchmark_data/BildeKrarup/B', 'benchmark_data/BildeKrarup/C', 'benchmark_data/BildeKrarup/Dq/1', 
					'benchmark_data/BildeKrarup/Dq/2', 'benchmark_data/BildeKrarup/Dq/3', 'benchmark_data/BildeKrarup/Dq/4', 
					'benchmark_data/BildeKrarup/Dq/5', 'benchmark_data/BildeKrarup/Dq/6', 'benchmark_data/BildeKrarup/Dq/7', 
					'benchmark_data/BildeKrarup/Dq/8', 'benchmark_data/BildeKrarup/Dq/9', 'benchmark_data/BildeKrarup/Dq/10', 
					'benchmark_data/BildeKrarup/Eq/1', 'benchmark_data/BildeKrarup/Eq/2', 'benchmark_data/BildeKrarup/Eq/3', 
					'benchmark_data/BildeKrarup/Eq/4', 'benchmark_data/BildeKrarup/Eq/5', 'benchmark_data/BildeKrarup/Eq/6', 
					'benchmark_data/BildeKrarup/Eq/7', 'benchmark_data/BildeKrarup/Eq/8', 'benchmark_data/BildeKrarup/Eq/9', 
					'benchmark_data/BildeKrarup/Eq/10']
	
	if chess:
		cartelle += ["benchmark_data/Chess"]
		
	if euclid:
		cartelle += ["benchmark_data/Euclid"]
		
	if fpp11:
		cartelle += ["benchmark_data/Fpp11"]
		
	if fpp17:
		cartelle += ["benchmark_data/Fpp17"]
		
	if koerkgosh_sym:
		cartell += ["benchmark_data/KoerkelGosh-sym/250/a", "benchmark_data/KoerkelGosh-sym/250/b", "benchmark_data/KoerkelGosh-sym/250/c", 
					"benchmark_data/KoerkelGosh-sym/500/a", "benchmark_data/KoerkelGosh-sym/500/b", "benchmark_data/KoerkelGosh-sym/500/c", 
					"benchmark_data/KoerkelGosh-sym/750/a", "benchmark_data/KoerkelGosh-sym/750/b", "benchmark_data/KoerkelGosh-sym/750/c"]
		
	return cartelle
	
def get_tests_string():
	tests = ""
	if bilde:
		tests += "bilde"
		
	if chess:
		tests += "chess"
		
	if euclid:
		tests += "euclid"
		
	if fpp11:
		tests += "fpp11"
		
	if fpp17:
		tests += "fpp17"
		
	if koerkgosh_sym:
		tests += "koerkgosh_sym"
		
	return tests
