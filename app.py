import streamlit as st
import streamlit.components.v1 as components
import time
import random

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Para Fufu 💖",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS PERSONALIZADO (Estética Ciberespacial y Romántica)
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Space+Mono&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1b0033 0%, #050514 100%);
        color: #e0e0e0;
        font-family: 'Space Mono', monospace;
    }
    h1, h2, h3 {
        font-family: 'Dancing Script', cursive;
        color: #ff99cc;
        text-shadow: 0px 0px 15px rgba(255, 153, 204, 0.6);
        text-align: center;
    }
    .poema-destacado {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 153, 204, 0.3);
        padding: 30px;
        border-radius: 15px;
        font-size: 1.2rem;
        line-height: 1.8;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8.5px);
        margin: 20px 0;
        font-style: italic;
    }
    .stButton>button {
        background: transparent;
        border: 2px solid #ff99cc;
        color: #ff99cc;
        border-radius: 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: #ff99cc;
        color: #050514;
        box-shadow: 0 0 20px #ff99cc;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL (Navegación Mágica)
# ==========================================
with st.sidebar:
    st.markdown("## 🧭 El Mapa de Nuestro Universo")
    menu = st.radio(
        "Elige un destino:",
        ("🌌 Ciberespacio 3D", "🧩 Acertijos del Corazón", "💌 Mensaje Principal")
    )
    st.markdown("---")
    st.markdown("### 🎵 Dale Play a Nuestra Canción")
    # Reproductor de música de YouTube (Married Life)
    st.video("https://youtu.be/7eQBm-j8Ev0?si=JHVEBaEXVIdFRQwW")
    st.markdown("<small style='text-align:center; display:block;'>Ponla de fondo mientras navegas Fufu...</small>", unsafe_allow_html=True)

# ==========================================
# SECCIÓN 1: CIBERESPACIO 3D (Three.js)
# ==========================================
if menu == "🌌 Ciberespacio 3D":
    st.markdown("<h1>El Universo de Fufu</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Navega por el espacio. Cada estrella brillante contiene algo especial. Haz clic o toca las estrellas más grandes para revelar lo que esconden.</p>", unsafe_allow_html=True)

    # Código HTML/JS para el universo en 3D con Three.js
    three_js_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body { margin: 0; overflow: hidden; background-color: #050514; }
            #poem-container {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: rgba(15, 12, 41, 0.85);
                border: 1px solid #ff99cc;
                padding: 30px;
                border-radius: 20px;
                color: white;
                font-family: 'Courier New', monospace;
                font-size: 1.2rem;
                text-align: center;
                display: none;
                z-index: 10;
                box-shadow: 0 0 30px #ff99cc;
                max-width: 80%;
            }
            #close-btn {
                margin-top: 20px;
                background: #ff99cc;
                color: black;
                border: none;
                padding: 10px 20px;
                border-radius: 10px;
                cursor: pointer;
                font-weight: bold;
            }
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="poem-container">
            <div id="poem-text"></div>
            <button id="close-btn" onclick="closePoem()">Cerrar</button>
        </div>
        <script>
            // Poemas para las estrellas
            const poemas = [
                "Puedes contar conmigo, y se que seremos y llegaremos a lo mismo o mejor que antes, yo cuando contigo para todo, tu eres mi psicologa y nadie cambiara eso, mi vista hacia ti es hermosa y eso no lo cambia nadie, eres la mejor y te amo",
                "Fufu, si el universo es infinito, mi amor por ti es el espacio en el que se expande.",
                "Eres la línea de código perfecta que resolvió todos mis errores.",
                "No hay constelación más hermosa que el reflejo de las estrellas en tus ojos.",
                "Cada latido de mi corazón está programado para amarte más que ayer.",
                "Eres mi refugio, mi lugar seguro, la chica que hace que todo tenga sentido."
            ];

            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x050514, 0.002);
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            // Estrellas de fondo (Pequeñas)
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 3000;
            const posArray = new Float32Array(particlesCount * 3);
            for(let i = 0; i < particlesCount * 3; i++) {
                posArray[i] = (Math.random() - 0.5) * 2000;
            }
            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            const particlesMaterial = new THREE.PointsMaterial({ size: 2, color: 0xffffff, transparent: true, opacity: 0.5 });
            const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
            scene.add(particlesMesh);

            // Estrellas interactivas (Grandes)
            const starsGroup = new THREE.Group();
            scene.add(starsGroup);
            const starGeometry = new THREE.SphereGeometry(2, 24, 24);
            const interactableStars = [];

            for(let i = 0; i < 30; i++) {
                const color = i % 2 === 0 ? 0xff99cc : 0x99ccff;
                const starMaterial = new THREE.MeshBasicMaterial({ color: color });
                const star = new THREE.Mesh(starGeometry, starMaterial);
                
                star.position.x = (Math.random() - 0.5) * 400;
                star.position.y = (Math.random() - 0.5) * 400;
                star.position.z = (Math.random() - 0.5) * 400;
                
                // Asignar poema (asegurando que el principal siempre esté)
                star.userData.poem = i === 0 ? poemas[0] : poemas[Math.floor(Math.random() * poemas.length)];
                
                starsGroup.add(star);
                interactableStars.push(star);
            }

            camera.position.z = 100;

            // Interacción (Raycaster)
            const raycaster = new THREE.Raycaster();
            const mouse = new THREE.Vector2();

            window.addEventListener('click', (event) => {
                mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
                mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
                raycaster.setFromCamera(mouse, camera);
                const intersects = raycaster.intersectObjects(starsGroup.children);
                
                if(intersects.length > 0) {
                    const selectedPoem = intersects[0].object.userData.poem;
                    document.getElementById("poem-text").innerText = selectedPoem;
                    document.getElementById("poem-container").style.display = "block";
                }
            });

            function closePoem() {
                document.getElementById("poem-container").style.display = "none";
            }

            // Animación
            let mouseX = 0;
            let mouseY = 0;
            document.addEventListener('mousemove', (event) => {
                mouseX = event.clientX - window.innerWidth / 2;
                mouseY = event.clientY - window.innerHeight / 2;
            });

            function animate() {
                requestAnimationFrame(animate);
                particlesMesh.rotation.y += 0.001;
                starsGroup.rotation.y += 0.002;
                starsGroup.rotation.x += 0.001;
                
                // Efecto parallax suave
                camera.position.x += (mouseX * 0.05 - camera.position.x) * 0.05;
                camera.position.y += (-mouseY * 0.05 - camera.position.y) * 0.05;
                camera.lookAt(scene.position);
                
                renderer.render(scene, camera);
            }
            animate();
        </script>
    </body>
    </html>
    """
    components.html(three_js_code, height=650)

# ==========================================
# SECCIÓN 2: ACERTIJOS Y JUEGOS
# ==========================================
elif menu == "🧩 Acertijos del Corazón":
    st.markdown("<h1>Juegos para mi Chica Especial</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔒 El Código del Amor", "✨ La Máquina de Recuerdos"])
    
    with tab1:
        st.markdown("### 🔐 Descifra el candado para un mensaje secreto")
        st.write("Si respondes bien estas tres preguntas, el sistema te dará una recompensa.")
        
        q1 = st.text_input("1. ¿Cuál es el nombre de la chica más hermosa que conozco? (Tu apodo)")
        q2 = st.text_input("2. ¿Qué se siente cuando estás conmigo? (Escribe: Paz, Amor o Magia)")
        
        if st.button("Desbloquear Sistema"):
            if q1.lower() in ["fufu", "fufi", "waffa"] and q2.lower() in ["paz", "amor", "magia"]:
                st.success("¡Acceso Concedido, mi amor!")
                st.balloons()
                st.markdown("""
                <div class="poema-destacado">
                    Has desbloqueado este rincón. Quiero que sepas que me encanta jugar contigo, reír contigo y compartir todo. Eres el nivel que siempre quise alcanzar en la vida y no quiero dejar de jugar este juego a tu lado.
                </div>
                """, unsafe_allow_html=True)
            elif q1 or q2:
                st.error("Mmm... intenta de nuevo, hermosa. Tú sabes la respuesta.")
    
    with tab2:
        st.markdown("### ✨ Conexión de Almas")
        st.write("Haz clic en el botón para ver cuánto estamos sincronizados hoy.")
        if st.button("Escanear Conexión"):
            with st.spinner("Analizando latidos, escaneando cariño..."):
                time.sleep(3)
            st.markdown(f"**Resultado del Escáner:** ¡Nuestra compatibilidad hoy es del **{random.randint(999, 1000)}%**! Es físicamente imposible amarte más, pero sé que mañana el porcentaje será aún mayor.")

# ==========================================
# SECCIÓN 3: MENSAJE PRINCIPAL
# ==========================================
elif menu == "💌 Mensaje Principal":
    st.markdown("<h1>Para Ti, Mi Todo</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div class="poema-destacado">
            <strong>"Puedes contar conmigo, y se que seremos y llegaremos a lo mismo o mejor que antes, yo cuando contigo para todo, tu eres mi psicologa y nadie cambiara eso, mi vista hacia ti es hermosa y eso no lo cambia nadie, eres la mejor y te amo"</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.write("""
        Creé este pequeño rincón del internet solo para nosotros. No importa qué tan vasto sea el mundo exterior, en este ciberespacio las estrellas brillan solo para ti. 
        
        Quería que tuvieras un lugar al que pudieras entrar cada vez que necesites recordar lo importante que eres. Con esta melodía de piano sonando, y estas palabras que escribí desde el alma, espero haberte sacado la sonrisa más hermosa del día.
        """)
        
        if st.button("Toca aquí para un último regalo"):
            st.snow()
            st.success("Mi corazón es tuyo. Siempre. 💖")

