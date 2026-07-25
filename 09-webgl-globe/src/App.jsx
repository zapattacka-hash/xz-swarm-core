import React, { useRef, useEffect, useState } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Stars } from '@react-three/drei';

const calcPos = (lat, lon, radius) => {
  const phi = (90 - lat) * (Math.PI / 180);
  const theta = (lon + 180) * (Math.PI / 180);
  const x = -(radius * Math.sin(phi) * Math.cos(theta));
  const z = (radius * Math.sin(phi) * Math.sin(theta));
  const y = radius * Math.cos(phi);
  return [x, y, z];
};

const SwarmGlobe = ({ data }) => {
  const meshRef = useRef();
  useFrame(() => (meshRef.current.rotation.y += 0.001));

  return (
    <group ref={meshRef}>
      <mesh>
        <sphereGeometry args={[2, 64, 64]} />
        <meshStandardMaterial color="#001122" wireframe={true} transparent opacity={0.6} />
      </mesh>
      {data.map((route, i) => (
        <React.Fragment key={i}>
          {/* Origin Node (Red) */}
          <mesh position={calcPos(route.origin_coords[0], route.origin_coords[1], 2.05)}>
            <sphereGeometry args={[0.04, 16, 16]} />
            <meshBasicMaterial color="#ff0000" />
          </mesh>
          {/* Transit Hub (Cyan) */}
          <mesh position={calcPos(route.transit_coords[0], route.transit_coords[1], 2.05)}>
            <sphereGeometry args={[0.06, 16, 16]} />
            <meshBasicMaterial color="#00ffcc" />
          </mesh>
        </React.Fragment>
      ))}
    </group>
  );
};

export default function App() {
  const [telemetry, setTelemetry] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/telemetry')
      .then(res => res.json())
      .then(res => { if (res.data) setTelemetry(res.data); })
      .catch(err => console.error("Bridge Offline", err));
  }, []);

  return (
    <div style={{ width: '100vw', height: '100vh', backgroundColor: '#0a0a0a' }}>
      <div style={{ position: 'absolute', top: 20, left: 20, color: '#00ffcc', fontFamily: 'monospace', zIndex: 10, pointerEvents: 'none' }}>
        <h2>XZ LABS: OMNI-SWARM TELEMETRY</h2>
        <p>ACTIVE RINGS: 43</p>
        <p style={{ color: telemetry.length ? '#00ffcc' : '#ff0000' }}>
          DB LINK: {telemetry.length ? "ESTABLISHED" : "SEARCHING..."}
        </p>
        <div style={{ marginTop: '20px' }}>
          {telemetry.map((t, i) => (
            <div key={i} style={{ marginBottom: 10, fontSize: '12px', borderLeft: '2px solid #ff0000', paddingLeft: 8 }}>
              <b>[ROUTE {i+1}]</b> {t.component}<br/>
              <span style={{color: '#ff0000'}}>{t.origin}</span> -> <span style={{color: '#00ffcc'}}>{t.transit}</span>
            </div>
          ))}
        </div>
      </div>
      <Canvas camera={{ position: [0, 0, 5] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={1} />
        <Stars radius={100} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
        <SwarmGlobe data={telemetry} />
        <OrbitControls enableZoom={true} />
      </Canvas>
    </div>
  );
}