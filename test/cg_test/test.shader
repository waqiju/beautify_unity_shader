CGPROGRAM
#pragma vertex vert
#pragma fragment frag

#include "UnityCG.cginc"

struct appdata_t
{
    float4 vertex : POSITION;
    fixed4 color : COLOR;
    float2 texcoord : TEXCOORD0;
};


struct v2f
{
    float4 vertex : SV_POSITION;
    fixed4 color : COLOR;
    float2 texcoord : TEXCOORD0;
};


sampler2D _MainTex;
uniform float4 _MainTex_ST;
uniform fixed4 _Color;
            
v2f vert (appdata_t v)
{
    v2f o;
    o.vertex = mul (UNITY_MATRIX_MVP, v.vertex);
    o.color = v.color * _Color;
    o.texcoord = TRANSFORM_TEX (v.texcoord, _MainTex);
//     // return o;
}



ENDCG