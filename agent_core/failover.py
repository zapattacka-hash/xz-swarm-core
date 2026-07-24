class RegionFailoverController:
    def __init__(self, primary: str = "us-east-1", secondary: str = "us-west-2"):
        self.primary = primary
        self.secondary = secondary
        self.active_region = primary

    def trigger_failover((self) -> str:
        self.active_region = self.secondary
        return f"ALERT: Failover triggered! Active region switched to '{self.active_region}'"

if __name__ == "__main__":
    fc = RegionFailoverController()
    print(f"Active Region: {fc.active_region}")
    print(fc.trigger_failover())
