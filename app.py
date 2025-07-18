import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_pendiente(x1, y1, x2, y2):
    """
    Calcula la pendiente entre dos puntos
    """
    if x2 - x1 == 0:
        return None  # Pendiente indefinida (línea vertical)
    return (y2 - y1) / (x2 - x1)

def ecuacion_recta(x1, y1, pendiente):
    """
    Calcula la ecuación de la recta en forma y = mx + b
    """
    if pendiente is None:
        return f"x = {x1}"
    b = y1 - pendiente * x1
    return f"y = {pendiente:.2f}x + {b:.2f}"

def main():
    st.title("📐 Calculadora de Pendiente entre Dos Puntos")
    st.write("Ingresa las coordenadas de dos puntos para calcular la pendiente de la recta que los conecta.")
    
    # Crear dos columnas para los puntos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Punto 1")
        x1 = st.number_input("Coordenada x₁:", value=0.0, step=0.1)
        y1 = st.number_input("Coordenada y₁:", value=0.0, step=0.1)
    
    with col2:
        st.subheader("Punto 2")
        x2 = st.number_input("Coordenada x₂:", value=1.0, step=0.1)
        y2 = st.number_input("Coordenada y₂:", value=1.0, step=0.1)
    
    # Calcular pendiente
    pendiente = calcular_pendiente(x1, y1, x2, y2)
    
    # Mostrar resultados
    st.subheader("📊 Resultados")
    
    if pendiente is None:
        st.error("⚠️ La pendiente es indefinida (línea vertical)")
        st.write(f"**Ecuación de la recta:** x = {x1}")
    else:
        st.success(f"**Pendiente (m):** {pendiente:.4f}")
        ecuacion = ecuacion_recta(x1, y1, pendiente)
        st.write(f"**Ecuación de la recta:** {ecuacion}")
        
        # Interpretar la pendiente
        if pendiente > 0:
            st.info("📈 Pendiente positiva: la recta es creciente")
        elif pendiente < 0:
            st.info("📉 Pendiente negativa: la recta es decreciente")
        else:
            st.info("➡️ Pendiente cero: la recta es horizontal")
    
    # Opción para mostrar el gráfico
    mostrar_grafico = st.checkbox("📈 Mostrar gráfico", value=True)
    
    if mostrar_grafico:
        st.subheader("🎨 Gráfico de la Recta")
        
        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Determinar el rango para el gráfico
        x_min = min(x1, x2) - 2
        x_max = max(x1, x2) + 2
        y_min = min(y1, y2) - 2
        y_max = max(y1, y2) + 2
        
        if pendiente is not None:
            # Crear puntos para la línea
            x_line = np.linspace(x_min, x_max, 100)
            b = y1 - pendiente * x1
            y_line = pendiente * x_line + b
            
            # Dibujar la recta
            ax.plot(x_line, y_line, 'b-', linewidth=2, label=f'y = {pendiente:.2f}x + {b:.2f}')
        else:
            # Línea vertical
            ax.axvline(x=x1, color='b', linewidth=2, label=f'x = {x1}')
        
        # Marcar los puntos
        ax.plot(x1, y1, 'ro', markersize=10, label=f'Punto 1 ({x1}, {y1})')
        ax.plot(x2, y2, 'go', markersize=10, label=f'Punto 2 ({x2}, {y2})')
        
        # Dibujar línea entre puntos
        ax.plot([x1, x2], [y1, y2], 'r--', alpha=0.7, linewidth=1)
        
        # Configurar el gráfico
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Recta que pasa por los dos puntos')
        ax.legend()
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        
        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
        
        # Información adicional
        with st.expander("ℹ️ Información adicional"):
            st.write("**Fórmula de la pendiente:**")
            st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}")
            st.write("**Interpretación:**")
            st.write("- Si m > 0: la recta es creciente")
            st.write("- Si m < 0: la recta es decreciente")
            st.write("- Si m = 0: la recta es horizontal")
            st.write("- Si m es indefinida: la recta es vertical")

if __name__ == "__main__":
    main()