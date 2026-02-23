# Technical Breakthrough: ARM NEON Parallelism

To run Artemis on a phone, we bypassed standard processing bottlenecks by:
- **Vectorization:** Using 128-bit SIMD (Single Instruction, Multiple Data) to process four 32-bit floats in a single cycle.
- **Recursive Logic:** Optimized for low-power mobile cores to prevent thermal throttling.
