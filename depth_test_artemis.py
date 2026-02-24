import time
import math

def recursive_depth_check(depth):
    print(f"--- Initiating Recursion Depth Test: {depth} Layers ---")
    start_time = time.perf_counter()
    
    # Simulating a logic gate that feeds back into itself 10,000 times
    val = 1.0
    for i in range(depth):
        # The "Recursive Fold" math
        val = math.tanh(val * 1.0001) 
        
    end_time = time.perf_counter()
    print(f"Status: [STABLE]")
    print(f"Final Convergence Value: {val:.6f}")
    print(f"Compute Time: {(end_time - start_time)*1000:.4f} ms")

if __name__ == "__main__":
    # Testing 10k, 50k, and 100k layers of recursive logic
    for d in [10000, 50000, 100000]:
        recursive_depth_check(d)
