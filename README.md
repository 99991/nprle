# nprle

`nprle` is a library for run-length-encoding binary masks.

A run-length encoding of a binary mask is a compact representation that
stores the counts of consecutive 0s and 1s in the mask.

For example, the binary mask

```
00 111 0000
```

would be encoded as

```
[2, 3, 4]
```

because it has 2 consecutive 0s, followed by 3 consecutive 1s, and then 4 consecutive 0s.

This representation reduces memory usage and speeds up operations like mean intersection over union (mIoU)
or binary operations (intersection/union/difference/xor),
which can be performed directly on the run-length-encoded masks.

All functions are vectorized with NumPy for better performance.

This library aims to be compatible with the masks from the [COCO dataset](https://cocodataset.org), which is why images use column-major order (configurable).

# Download and run example

```bash
pip install numpy pillow
git clone https://github.com/99991/nprle.git
cd nprle
python test.py
python example.py
```

# Example

```python
from PIL import Image
import numpy as np
from nprle import rle_encode, rle_decode, rle_miou, rle_intersect, rle_area

# Load binary masks as NumPy arrays
mask1 = np.array(Image.open("data/binary_mask1.png"))
mask2 = np.array(Image.open("data/binary_mask2.png"))

# Run-length-encode binary masks count number of consecutive 0 and 1 bits
counts1 = rle_encode(mask1)
counts2 = rle_encode(mask2)

shape = mask1.shape

print(f"mask1 of shape {shape} requires {mask1.nbytes/1000:.1f} KB using {mask1.dtype}.")

# Run-length encoding can save a lot of memory (97 % in this case)
percent = 100 * counts1.nbytes / mask1.nbytes
print(f"counts1 only requires {counts1.nbytes/1000:.1f} KB ({100 - percent:.0f} % reduction) using {counts1.dtype}.")

# Decoding example
mask1_decoded = rle_decode(counts1, shape)
mask2_decoded = rle_decode(counts2, shape)

assert np.array_equal(mask1, mask1_decoded)
assert np.array_equal(mask2, mask2_decoded)

# Computing mean intersection over union using run-length-encoding is very fast
miou = rle_miou(counts1, counts2)

print(f"mIoU (mean intersection over union) of both masks is {miou*100:.1f} %")

intersection = rle_intersect(counts1, counts2)

num_overlapping_pixels = rle_area(intersection)

print(f"{num_overlapping_pixels} pixels are equal to 1 in both masks at once.")
```

# Benchmark

For larger images, the advantage of using run-length-encoding becomes more pronounced
when compared to traditional pixel-wise operations. The following graph shows the
performance of various operations in relation to increasing image sizes.

Since run-length-encoding is relatively costly (still cheap though), it is recommended to store binary masks in this format so that encoding only needs to be done once.

![benchmark](https://github.com/user-attachments/assets/0829bc9e-128f-4d54-b513-11e8d6f49f06)
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="695.834707pt" height="411.03625pt" viewBox="0 0 695.834707 411.03625" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2025-08-06T22:23:07.765068</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.10.3, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 411.03625 
L 695.834707 411.03625 
L 695.834707 0 
L 0 0 
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 44.898125 379.96 
L 695.114707 379.96 
L 695.114707 0.72 
L 44.898125 0.72 
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <defs>
       <path id="m2a14059604" d="M 0 0 
L 0 3.5 
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m2a14059604" x="74.453424" y="379.96" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="74.453424" y="394.558437" transform="rotate(-0 74.453424 394.558437)">128x128</text>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_2">
      <g>
       <use xlink:href="#m2a14059604" x="192.674621" y="379.96" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="192.674621" y="394.558437" transform="rotate(-0 192.674621 394.558437)">256x256</text>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_3">
      <g>
       <use xlink:href="#m2a14059604" x="310.895818" y="379.96" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="310.895818" y="394.558437" transform="rotate(-0 310.895818 394.558437)">512x512</text>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_4">
      <g>
       <use xlink:href="#m2a14059604" x="429.117015" y="379.96" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="429.117015" y="394.558437" transform="rotate(-0 429.117015 394.558437)">1024x1024</text>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_5">
      <g>
       <use xlink:href="#m2a14059604" x="547.338211" y="379.96" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="547.338211" y="394.558437" transform="rotate(-0 547.338211 394.558437)">2048x2048</text>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_6">
      <g>
       <use xlink:href="#m2a14059604" x="665.559408" y="379.96" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="665.559408" y="394.558437" transform="rotate(-0 665.559408 394.558437)">4096x4096</text>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_7">
      <defs>
       <path id="m31948205b5" d="M 0 0 
L 0 2 
" style="stroke: #000000; stroke-width: 0.6"/>
      </defs>
      <g>
       <use xlink:href="#m31948205b5" x="150.570874" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_8">
      <g>
       <use xlink:href="#m31948205b5" x="219.72584" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_9">
     <g id="line2d_9">
      <g>
       <use xlink:href="#m31948205b5" x="268.79207" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_10">
     <g id="line2d_10">
      <g>
       <use xlink:href="#m31948205b5" x="306.850795" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_11">
     <g id="line2d_11">
      <g>
       <use xlink:href="#m31948205b5" x="337.947037" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_12">
     <g id="line2d_12">
      <g>
       <use xlink:href="#m31948205b5" x="364.238535" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_13">
     <g id="line2d_13">
      <g>
       <use xlink:href="#m31948205b5" x="387.013267" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_14">
     <g id="line2d_14">
      <g>
       <use xlink:href="#m31948205b5" x="407.102004" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_15">
     <g id="line2d_15">
      <g>
       <use xlink:href="#m31948205b5" x="543.293189" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_16">
     <g id="line2d_16">
      <g>
       <use xlink:href="#m31948205b5" x="612.448156" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="xtick_17">
     <g id="line2d_17">
      <g>
       <use xlink:href="#m31948205b5" x="661.514385" y="379.96" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="text_7">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="370.006416" y="408.236562" transform="rotate(-0 370.006416 408.236562)">Image size</text>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_18">
      <defs>
       <path id="m7ad6ef4454" d="M 0 0 
L -3.5 0 
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m7ad6ef4454" x="44.898125" y="349.344619" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- $\mathdefault{10^{-5}}$ -->
      <g transform="translate(14.398125 353.143838)">
       <text>
        <tspan x="0" y="-0.064063" style="font-size: 10px; font-family: 'DejaVu Sans'">1</tspan>
        <tspan x="6.362305" y="-0.064063" style="font-size: 10px; font-family: 'DejaVu Sans'">0</tspan>
        <tspan x="12.820312" y="-3.892188" style="font-size: 7px; font-family: 'DejaVu Sans'">−</tspan>
        <tspan x="18.685547" y="-3.892188" style="font-size: 7px; font-family: 'DejaVu Sans'">5</tspan>
       </text>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_19">
      <g>
       <use xlink:href="#m7ad6ef4454" x="44.898125" y="273.648117" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- $\mathdefault{10^{-4}}$ -->
      <g transform="translate(14.398125 277.447336)">
       <text>
        <tspan x="0" y="-0.064063" style="font-size: 10px; font-family: 'DejaVu Sans'">1</tspan>
        <tspan x="6.362305" y="-0.064063" style="font-size: 10px; font-family: 'DejaVu Sans'">0</tspan>
        <tspan x="12.820312" y="-3.892188" style="font-size: 7px; font-family: 'DejaVu Sans'">−</tspan>
        <tspan x="18.685547" y="-3.892188" style="font-size: 7px; font-family: 'DejaVu Sans'">4</tspan>
       </text>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_20">
      <g>
       <use xlink:href="#m7ad6ef4454" x="44.898125" y="197.951615" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_10">
      <!-- $\mathdefault{10^{-3}}$ -->
      <g transform="translate(14.398125 201.750833)">
       <text>
        <tspan x="0" y="-0.976562" style="font-size: 10px; font-family: 'DejaVu Sans'">1</tspan>
        <tspan x="6.362305" y="-0.976562" style="font-size: 10px; font-family: 'DejaVu Sans'">0</tspan>
        <tspan x="12.820312" y="-4.804688" style="font-size: 7px; font-family: 'DejaVu Sans'">−</tspan>
        <tspan x="18.685547" y="-4.804688" style="font-size: 7px; font-family: 'DejaVu Sans'">3</tspan>
       </text>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_21">
      <g>
       <use xlink:href="#m7ad6ef4454" x="44.898125" y="122.255113" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- $\mathdefault{10^{-2}}$ -->
      <g transform="translate(14.398125 126.054331)">
       <text>
        <tspan x="0" y="-0.976562" style="font-size: 10px; font-family: 'DejaVu Sans'">1</tspan>
        <tspan x="6.362305" y="-0.976562" style="font-size: 10px; font-family: 'DejaVu Sans'">0</tspan>
        <tspan x="12.820312" y="-4.804688" style="font-size: 7px; font-family: 'DejaVu Sans'">−</tspan>
        <tspan x="18.685547" y="-4.804688" style="font-size: 7px; font-family: 'DejaVu Sans'">2</tspan>
       </text>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_22">
      <g>
       <use xlink:href="#m7ad6ef4454" x="44.898125" y="46.55861" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- $\mathdefault{10^{-1}}$ -->
      <g transform="translate(14.398125 50.357829)">
       <text>
        <tspan x="0" y="-0.064063" style="font-size: 10px; font-family: 'DejaVu Sans'">1</tspan>
        <tspan x="6.362305" y="-0.064063" style="font-size: 10px; font-family: 'DejaVu Sans'">0</tspan>
        <tspan x="12.820312" y="-3.892188" style="font-size: 7px; font-family: 'DejaVu Sans'">−</tspan>
        <tspan x="18.685547" y="-3.892188" style="font-size: 7px; font-family: 'DejaVu Sans'">1</tspan>
       </text>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_23">
      <defs>
       <path id="me73a1bdbb3" d="M 0 0 
L -2 0 
" style="stroke: #000000; stroke-width: 0.6"/>
      </defs>
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="379.467286" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_7">
     <g id="line2d_24">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="372.131537" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_8">
     <g id="line2d_25">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="366.137793" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_9">
     <g id="line2d_26">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="361.070156" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_10">
     <g id="line2d_27">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="356.680368" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_11">
     <g id="line2d_28">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="352.808301" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_12">
     <g id="line2d_29">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="326.557701" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_13">
     <g id="line2d_30">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="313.228209" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_14">
     <g id="line2d_31">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="303.770784" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_15">
     <g id="line2d_32">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="296.435035" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_16">
     <g id="line2d_33">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="290.441291" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_17">
     <g id="line2d_34">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="285.373653" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_18">
     <g id="line2d_35">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="280.983866" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_19">
     <g id="line2d_36">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="277.111799" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_20">
     <g id="line2d_37">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="250.861199" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_21">
     <g id="line2d_38">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="237.531707" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_22">
     <g id="line2d_39">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="228.074281" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_23">
     <g id="line2d_40">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="220.738532" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_24">
     <g id="line2d_41">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="214.744789" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_25">
     <g id="line2d_42">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="209.677151" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_26">
     <g id="line2d_43">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="205.287364" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_27">
     <g id="line2d_44">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="201.415297" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_28">
     <g id="line2d_45">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="175.164697" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_29">
     <g id="line2d_46">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="161.835205" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_30">
     <g id="line2d_47">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="152.377779" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_31">
     <g id="line2d_48">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="145.04203" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_32">
     <g id="line2d_49">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="139.048287" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_33">
     <g id="line2d_50">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="133.980649" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_34">
     <g id="line2d_51">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="129.590862" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_35">
     <g id="line2d_52">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="125.718794" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_36">
     <g id="line2d_53">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="99.468195" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_37">
     <g id="line2d_54">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="86.138702" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_38">
     <g id="line2d_55">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="76.681277" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_39">
     <g id="line2d_56">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="69.345528" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_40">
     <g id="line2d_57">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="63.351785" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_41">
     <g id="line2d_58">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="58.284147" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_42">
     <g id="line2d_59">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="53.894359" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_43">
     <g id="line2d_60">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="50.022292" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_44">
     <g id="line2d_61">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="23.771693" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_45">
     <g id="line2d_62">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="10.4422" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="ytick_46">
     <g id="line2d_63">
      <g>
       <use xlink:href="#me73a1bdbb3" x="44.898125" y="0.984775" style="stroke: #000000; stroke-width: 0.6"/>
      </g>
     </g>
    </g>
    <g id="text_13">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: middle" x="8.318438" y="190.34" transform="rotate(-90 8.318438 190.34)">Time [seconds]</text>
    </g>
   </g>
   <g id="line2d_64">
    <path d="M 74.453424 301.110091 
L 192.674621 260.031028 
L 310.895818 216.877104 
L 429.117015 158.149868 
L 547.338211 105.249062 
L 665.559408 17.958182 
" clip-path="url(#p82942b52a7)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_65">
    <path d="M 74.453424 304.997418 
L 192.674621 261.593352 
L 310.895818 216.455671 
L 429.117015 158.063326 
L 547.338211 104.659857 
L 665.559408 24.60639 
" clip-path="url(#p82942b52a7)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_66">
    <path d="M 74.453424 288.351991 
L 192.674621 281.247505 
L 310.895818 273.048399 
L 429.117015 260.705969 
L 547.338211 240.891208 
L 665.559408 222.711165 
" clip-path="url(#p82942b52a7)" style="fill: none; stroke: #2ca02c; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_67">
    <path d="M 74.453424 362.721818 
L 192.674621 359.501994 
L 310.895818 356.812132 
L 429.117015 353.738161 
L 547.338211 338.334942 
L 665.559408 333.662095 
" clip-path="url(#p82942b52a7)" style="fill: none; stroke: #d62728; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_68">
    <path d="M 74.453424 291.712602 
L 192.674621 285.421591 
L 310.895818 275.071039 
L 429.117015 266.127999 
L 547.338211 250.870405 
L 665.559408 229.463664 
" clip-path="url(#p82942b52a7)" style="fill: none; stroke: #9467bd; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_69">
    <path d="M 74.453424 312.479586 
L 192.674621 278.277729 
L 310.895818 236.853749 
L 429.117015 193.273719 
L 547.338211 144.345177 
L 665.559408 94.983479 
" clip-path="url(#p82942b52a7)" style="fill: none; stroke: #8c564b; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 44.898125 379.96 
L 44.898125 0.72 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 695.114707 379.96 
L 695.114707 0.72 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 44.898125 379.96 
L 695.114707 379.96 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 44.898125 0.72 
L 695.114707 0.72 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="legend_1">
    <g id="patch_7">
     <path d="M 51.898125 98.179375 
L 174.959063 98.179375 
Q 176.959063 98.179375 176.959063 96.179375 
L 176.959063 7.72 
Q 176.959063 5.72 174.959063 5.72 
L 51.898125 5.72 
Q 49.898125 5.72 49.898125 7.72 
L 49.898125 96.179375 
Q 49.898125 98.179375 51.898125 98.179375 
z
" style="fill: #ffffff; opacity: 0.8; stroke: #cccccc; stroke-linejoin: miter"/>
    </g>
    <g id="line2d_70">
     <path d="M 53.898125 13.818437 
L 63.898125 13.818437 
L 73.898125 13.818437 
" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_14">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: start" x="81.898125" y="17.318437" transform="rotate(-0 81.898125 17.318437)">rle_encode mask1</text>
    </g>
    <g id="line2d_71">
     <path d="M 53.898125 28.774687 
L 63.898125 28.774687 
L 73.898125 28.774687 
" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_15">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: start" x="81.898125" y="32.274687" transform="rotate(-0 81.898125 32.274687)">rle_encode mask2</text>
    </g>
    <g id="line2d_72">
     <path d="M 53.898125 43.730937 
L 63.898125 43.730937 
L 73.898125 43.730937 
" style="fill: none; stroke: #2ca02c; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_16">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: start" x="81.898125" y="47.230937" transform="rotate(-0 81.898125 47.230937)">rle_intersect</text>
    </g>
    <g id="line2d_73">
     <path d="M 53.898125 58.687187 
L 63.898125 58.687187 
L 73.898125 58.687187 
" style="fill: none; stroke: #d62728; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_17">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: start" x="81.898125" y="62.187187" transform="rotate(-0 81.898125 62.187187)">rle_area</text>
    </g>
    <g id="line2d_74">
     <path d="M 53.898125 73.643437 
L 63.898125 73.643437 
L 73.898125 73.643437 
" style="fill: none; stroke: #9467bd; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_18">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: start" x="81.898125" y="77.143437" transform="rotate(-0 81.898125 77.143437)">rle_miou</text>
    </g>
    <g id="line2d_75">
     <path d="M 53.898125 88.599687 
L 63.898125 88.599687 
L 73.898125 88.599687 
" style="fill: none; stroke: #8c564b; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_19">
     <text style="font-size: 10px; font-family: 'DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', sans-serif; text-anchor: start" x="81.898125" y="92.099687" transform="rotate(-0 81.898125 92.099687)">NumPy mIoU</text>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p82942b52a7">
   <rect x="44.898125" y="0.72" width="650.216582" height="379.24"/>
  </clipPath>
 </defs>
</svg>
