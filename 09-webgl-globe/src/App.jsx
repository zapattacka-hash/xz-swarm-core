import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Stars } from '@react-three/drei';

const SwarmGlobe = () => {
  const meshRef = useRef();
  useFrame(() => (meshRef.current.rotation.y += 0.002));

  return (
    <mesh ref={meshRef}>
      <sphereGeometry args={[2, 64, 64]} />
      <meshStandardMaterial color="#00ffcc" wireframe={true} />
    </mesh>
  );
};

export default function App() {
  return (
    <div style={{ width: '100vw', height: '100vh', backgroundColor: '#0a0a0a' }}>
      <div style={{ position: 'absolute', top: 20, left: 20, color: '#00ffcc', fontFamily: 'monospace', zIndex: 10 }}>
        <h2>XZ LABS: OMNI-SWARM TELEMETRY</h2>
        <p>ACTIVE RINGS: 43</p>
        <p>TARGETING VECTOR: AWAITING INPUT...</p>
      </div>
      <Canvas camera={{ position: [0, 0, 5] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={1} />
        <Stars radius={100} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
        <SwarmGlobe />
        <OrbitControls enableZoom={true} />
      </Canvas>
    </div>
  );
}
