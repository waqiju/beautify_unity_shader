
        CGPROGRAM
        #pragma surface surf NoLighting alpha
        //alpha:blend is key because shader uses mask texture's alpha for "filling" mechanism

        //Custom lightning function to prevent any light from affecting the globe
        fixed4 LightingNoLighting(SurfaceOutput s, fixed3 lightDir, fixed atten)
        {
            fixed4 c;
            c.rgb = s.Albedo;
            c.a = s.Alpha;
            return c;
        }


        

        sampler2D _MaskTex;
        sampler2D _MainTex;
        sampler2D _MainTex2;
        sampler2D _MainTex3;
        sampler2D _HotlineTex;

        float _Progress;

        half _LAYER_1_SCROLL_Y;
        half _LAYER_1_SCROLL_X;
        half _LAYER_2_SCROLL_Y;
        half _LAYER_2_SCROLL_X;
        half _LAYER_3_SCROLL_Y;
        half _LAYER_3_SCROLL_X;

        fixed4 _Color;
        fixed4 _HotlineColor;

        struct Input {
            float2 uv_MaskTex;
            float2 uv_MainTex;
            float2 uv_MainTex2;
            float2 uv_MainTex3;
            float2 uv_HotlineTex;
        };


        void surf(Input IN, inout SurfaceOutput o) {
            //next 3 lines scroll texture by altering x and y using _Time[1]
            float2 uv1 = float2(IN.uv_MainTex.x + _Time[1] * _LAYER_1_SCROLL_X, IN.uv_MainTex.y + _Time[1] * _LAYER_1_SCROLL_Y);
            float2 uv2 = float2(IN.uv_MainTex2.x + _Time[1] * _LAYER_2_SCROLL_X, IN.uv_MainTex2.y + _Time[1] * _LAYER_2_SCROLL_Y);
            float2 uv3 = float2(IN.uv_MainTex3.x + _Time[1] * _LAYER_3_SCROLL_X, IN.uv_MainTex3.y + _Time[1] * _LAYER_3_SCROLL_Y);

            //place the hotline texture to the where the progress value is 
            float2 uvx = float2(IN.uv_HotlineTex.x + _Time[0], IN.uv_HotlineTex.y - _Progress);
            //offset mask texture using the same logic from above
            float2 uvmasx = float2(IN.uv_MaskTex.x, IN.uv_MaskTex.y - _Progress);

            //multiply textures by each other and color
            fixed4 c = tex2D(_MainTex, uv1) * tex2D(_MainTex2, uv2) * tex2D(_MainTex, uv2 + 0.3)  * tex2D(_MainTex3, uv3) * _Color;
            fixed4 a = tex2D(_MaskTex, uvmasx);
            fixed4 x = tex2D(_HotlineTex, uvx) * _HotlineColor;

            //multiply color "C" by color "A" darkens down the result so we multiply it by "3" to brighten it up
            c = c  * a * 3;
            // (c * x * 5) add more color to the white hotline
            // the "2" in the "x.a * 2" once against brightens the result
            // _HotlineColor.a alters hotlines transparency
            c = c + ((c * x * 5) + x) * x.a * 2 * _HotlineColor.a;
            o.Albedo = c.rgb;
            o.Alpha = c.a;
        }
        ENDCG