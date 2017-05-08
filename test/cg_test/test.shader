    CGINCLUDE
    #pragma vertex vert
    #pragma fragment frag
    #pragma target 2.0
    #pragma multi_compile _ UNITY_SINGLE_PASS_STEREO
    #pragma multi_compile ___ STEREO_INSTANCING_ON 
    #include "UnityCG.cginc"

    struct appdata_t {
        float4 vertex : POSITION;
        fixed4 color : COLOR;
        // UNITY_VERTEX_INPUT_INSTANCE_ID
    };

    struct v2f {
        float4 vertex : SV_POSITION;
        fixed4 color : COLOR;
        // UNITY_VERTEX_OUTPUT_STEREO
    };

    v2f vert (appdata_t v)
    {
        UNITY_SETUP_INSTANCE_ID(v);
        v2f o;
        UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o);
        o.vertex = UnityObjectToClipPos(v.vertex);
        o.color = v.color;
        return o;
    }

    fixed4 frag (v2f i) : SV_Target
    {
        return i.color;
    }
    ENDCG 