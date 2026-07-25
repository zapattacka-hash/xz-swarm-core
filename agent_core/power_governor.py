class PowerGovernor:
    @staticmethod
    def adjust_tick_rate(battery_pct: float, thermal_celsius: float) -> float:
        if battery_pct < 20.0 or thermal_celsius > 75.0:
            return 0.5  # Throttled low-power mode
        return 0.05      # High-performance mode

if __name__ == "__main__":
    print(f"Optimal Tick Rate (Normal) : {PowerGovernor.adjust_tick_rate(90.0, 45.0)}s")
    print(f"Optimal Tick Rate (Thermal): {PowerGovernor.adjust_tick_rate(15.0, 80.0)}s")
