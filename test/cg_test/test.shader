CGPROGRAM

			

			fixed4 frag (g2f i) : SV_Target
			{

				
				const fixed4 colors[11] = { 
						fixed4(1.0, 1.0, 1.0, 1.0),  // White
						fixed4(1.0, 0.0, 0.0, 1.0),  // Red
						fixed4(0.0, 1.0, 0.0, 1.0),  // Green
						fixed4(0.0, 0.0, 1.0, 1.0),  // Blue
						fixed4(1.0, 1.0, 0.0, 1.0),  // Yellow
						fixed4(0.0, 1.0, 1.0, 1.0),  // Cyan/Aqua
						fixed4(1.0, 0.0, 1.0, 1.0),  // Magenta
						fixed4(0.5, 0.0, 0.0, 1.0),  // Maroon
						fixed4(0.0, 0.5, 0.5, 1.0),  // Teal
						fixed4(1.0, 0.65, 0.0, 1.0), // Orange
						fixed4(1.0, 1.0, 1.0, 1.0)   // White
					};

			}
			ENDCG