    CGPROGRAM

    fixed4 frag(g2fi) : SV_Target
    {

        constfixed4 colors[11]={fixed4(1.0, 1.0, 1.0, 1.0),fixed4(1.0, 0.0, 0.0, 1.0),fixed4(0.0, 1.0, 0.0, 1.0),fixed4(0.0, 0.0, 1.0, 1.0),fixed4(1.0, 1.0, 0.0, 1.0),fixed4(0.0, 1.0, 1.0, 1.0),fixed4(1.0, 0.0, 1.0, 1.0),fixed4(0.5, 0.0, 0.0, 1.0),fixed4(0.0, 0.5, 0.5, 1.0),fixed4(1.0, 0.65, 0.0, 1.0),fixed4(1.0, 1.0, 1.0, 1.0)};
    }

    // White
    ENDCG
