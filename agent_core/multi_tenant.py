class MultiTenantIsolator:
    def __init__(self):
        self.tenants = {}

    def register_tenant(self, tenant_id: str):
        self.tenants[tenant_id] = []

    def route_payload(self, tenant_id: str, payload: dict) -> bool:
        if tenant_id in self.tenants:
            self.tenants[tenant_id].append(payload)
            return True
        return False

if __name__ == "__main__":
    mt = MultiTenantIsolator()
    mt.register_tenant("enterprise-alpha")
    print("Payload Routed:", mt.route_payload("enterprise-alpha", {"data": "q_state"}))
