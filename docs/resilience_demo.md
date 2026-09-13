# Resilience Demonstration

## Retry Policy Demonstration

Attempt 1 → Failed

Attempt 2 → Failed

Attempt 3 → Recovered Successfully

Configuration:
- Max Attempts = 5
- Initial Interval = 1s
- Max Interval = 8s
- Jitter = Enabled

The retry mechanism successfully recovered from a simulated transient failure within the configured retry limit.

---

## Node Timeout Demonstration

NODE STARTED

TIMEOUT DETECTED

Function exceeded 3 seconds

The per-node timeout prevented a long-running operation from hanging indefinitely.

---

## Global Timeout Demonstration

NODE 1 STARTED

NODE 1 FINISHED

NODE 2 STARTED

Global timeout exceeded (5 seconds)

The global timeout successfully cancelled the graph execution when the total execution time exceeded the configured limit.