from setup import *

def get_folders_list():
	cartelle = []
	
	if test1:
		cartelle.append(["benchmark_data/test/test1","benchmark_data/test/test3"])
	
	if test2:
		cartelle.append(["benchmark_data/test/test2"])
	
	
	
	
	
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
		
	if koerkgosh_sym:
		cartelle.append(["benchmark_data/KoerkelGosh-sym/250/a", "benchmark_data/KoerkelGosh-sym/250/b", "benchmark_data/KoerkelGosh-sym/250/c", 
					"benchmark_data/KoerkelGosh-sym/500/a", "benchmark_data/KoerkelGosh-sym/500/b", "benchmark_data/KoerkelGosh-sym/500/c", 
					"benchmark_data/KoerkelGosh-sym/750/a", "benchmark_data/KoerkelGosh-sym/750/b", "benchmark_data/KoerkelGosh-sym/750/c"])

	if koerkgosh_assym:
		cartelle.append(["benchmark_data/KoerkelGosh-assym/250/a", "benchmark_data/KoerkelGosh-assym/250/b", "benchmark_data/KoerkelGosh-assym/250/c", 
					"benchmark_data/KoerkelGosh-assym/500/a", "benchmark_data/KoerkelGosh-assym/500/b", "benchmark_data/KoerkelGosh-assym/500/c", 
					"benchmark_data/KoerkelGosh-assym/750/a", "benchmark_data/KoerkelGosh-assym/750/b", "benchmark_data/KoerkelGosh-assym/750/c"])
	if gapa:
		cartelle.append(["benchmark_data/GapA"])
	
	if gapb:
		cartelle.append(["benchmark_data/GapB"])
		
	if gapc:
		cartelle.append(["benchmark_data/GapC"])
		
	
	return cartelle
	
def get_tests_list():
	tests = []
	
	if test1:
		tests.append("test1")
	
	if test2:
		tests.append("test2")
	
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
		
	if koerkgosh_sym:
		tests.append("koerkgosh_sym")
		
	if koerkgosh_assym:
		tests.append("koerkgosh_assym")
		
	if gapa:
		tests.append("gapa")
		
	if gapb:
		tests.append("gapb")
		
	if gapc:
		tests.append("gapc")
		
	return tests
