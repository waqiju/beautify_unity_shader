Shader "Test/Formater"{
Properties    {
_MainTex("Main Text",2D)="white"{}
_Cutoff("Cutoff",Range(0,1))=0.5
_Color("Color",Color)=(1,1,1,1)
[Enum(UV0,0,UV1,1)] _UVSec ("UV Set for secondary textures",Float) = 0
[MaterialEnum(None,0,Fastest,1,Fast,2,Better,3,Best,4,Palm,5)] _WindQuality ("Wind Quality",Range(0,5)) = 0
[KeywordEnum(None,Simple,High Quality)] _SunDisk ("Sun",Int) = 2
[MaterialToggle] PixelSnap ("Pixel snap",Float) = 0
[Toggle(UNITY_UI_ALPHACLIP)] _UseUIAlphaClip ("Use Alpha Clip",Float) = 0
[MaterialToggle] PixelSnap ("Pixel snap",Float) = 0
[ToggleOff] _GlossyReflections ("Glossy Reflections",Float) = 1.0
}
Category{
Blend One OneMinusSrcAlpha
}
SubShader{
// ---- cmd_stm -----
AlphaToMask True ColorMask RGB AlphaTest off AlphaTest Greater [_Cutoff] 
BindChannels {
Bind "Vertex", vertex Bind "normal", normal
// lightmap uses 2nd uv
Bind "texcoord1", texcoord0 
// unused
Bind "texcoord1", texcoord1 
// main uses 1st uv
Bind "texcoord", texcoord2
}
Blend Off     Blend One OneMinusSrcAlpha     Fog { Mode off }
// in additive pass fog should be black
Fog { Color (0, 0, 0, 0) } 
Material{
Diffuse [_Color]
Ambient [_Color]
Shininess [_Shininess]
Specular [_SpecColor]
Emission [_Emission]
}
Name "BASE"
Offset [_ZBias], [_ZBias]
Stencil { Comp Always Pass Zero }
SetTexture [_MainTex] { 
combine texture * primaryDOUBLE, texture * primary
}
SetTexture [unity_Lightmap] { 
matrix [unity_LightmapMatrix] constantColor [_Color] combine texture * constant
}
Tags {
"RenderType" = "TreeOpaque"
"DisableBatching" = "True"
}
// ---- cmd_stm ----

// ---- shr_pass ----
GrabPass {
Name "BASE"
Tags{
"LightMode" = "Always"
}}

UsePass "Reflective/Bumped Unlit/BASE"

Pass
{
CGPROGRAM
#pragma vertex vert
#pragma fragment frag
#pragma multi_compile_particles
#pragma multi_compile_fog

#include "UnityCG.cginc"

sampler2D _MainTex;

fixed4 _TintColor;

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
UNITY_FOG_COORDS(1)
#ifdef SOFTPARTICLES_ON
float4 projPos : TEXCOORD2;
#endif
};

float4 _MainTex_ST;

v2f vert(appdata_t v)
{
v2f o;
o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);
#ifdef SOFTPARTICLES_ON
o.projPos = ComputeScreenPos(o.vertex);
COMPUTE_EYEDEPTH(o.projPos.z);
#endif
o.color = v.color;
o.texcoord = TRANSFORM_TEX(v.texcoord, _MainTex);
UNITY_TRANSFER_FOG(o, o.vertex);
return o;
}

sampler2D_float _CameraDepthTexture;
float _InvFade;

fixed4 frag(v2f i) : SV_Target
{
#ifdef SOFTPARTICLES_ON
float sceneZ = LinearEyeDepth(SAMPLE_DEPTH_TEXTURE_PROJ(_CameraDepthTexture, UNITY_PROJ_COORD(i.projPos)));
float partZ = i.projPos.z;
float fade = saturate(_InvFade * (sceneZ - partZ));
i.color.a *= fade;
#endif

fixed4 col = 2.0f * i.color * _TintColor * tex2D(_MainTex, i.texcoord);
// fog towards black due to our blend mode
UNITY_APPLY_FOG_COLOR(i.fogCoord, col, fixed4(0, 0, 0, 0));
return col;
}
ENDCG
}

    Pass
    {
        CGPROGRAM
        #pragma vertex vert
        #pragma fragment frag
        #include "UnityCG.cginc"
        struct v2f
        {
            float4 pos : SV_POSITION;
            float4 nz : TEXCOORD0;
        };

        v2f vert(appdata_base v)
        {
            v2f o;
            o.pos = mul(UNITY_MATRIX_MVP, v.vertex);
            o.nz.xyz = COMPUTE_VIEW_NORMAL;
            o.nz.w = COMPUTE_DEPTH_01;
            return o;
        }

        fixed4 frag(v2f i) : SV_Target
        {
            return EncodeDepthNormal(i.nz.w, i.nz.xyz);
        }
        ENDCG
    }
    // ---- shr_pass ----
}

FallBack Off
FallBack "Legacy Shaders/Transparent/Diffuse"
CustomEditor "LegacyIlluminShaderGUI"
Dependency "BaseMapShader" = "Hidden/TerrainEngine/Splatmap/Standard-Base"
}