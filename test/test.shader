Shader "GUI/Text Shader"
{
    Properties
    {
        _MainTex ("Font Texture", 2D) = "white" {  }
        _Color ("Text Color", Color) = (1, 1, 1, 1)
    }
    SubShader
    {
        Tags
        {
            "Queue" = "Transparent"
            "IgnoreProjector" = "True"
            "RenderType" = "Transparent"
            "PreviewType" = "Plane"
        }
    }
}
