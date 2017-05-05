CGPROGRAM
#pragma vertex vert
#pragma fragment frag

#include "UnityCG.cginc"

// struct appdata_t
// {
//     float4 vertex : POSITION;
//     fixed4 color : COLOR;
//     float2 texcoord : TEXCOORD0;
// };


// struct v2f
// {
//     float4 vertex : SV_POSITION;
//     fixed4 color : COLOR;
//     float2 texcoord : TEXCOORD0;
// };


sampler2D _MainTex;
// uniform float4 _MainTex_ST;
// uniform fixed4 _Color;

ENDCG