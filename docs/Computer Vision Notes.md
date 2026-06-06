

# 1 — Homogeneous Coordinates for Computer Graphics

**Definition:**  
Homogeneous coordinates (or projective coordinates), introduced by **August Ferdinand Möbius** in 1827, are a system of coordinates used in **projective geometry**, just as Cartesian coordinates are used in Euclidean geometry.

Think of homogeneous coordinates as a **mathematical trick** that makes transformations in computer graphics uniform and easier to handle.

---

## 🔹 Why we use them

In **Cartesian coordinates**:

| Transformation | Can be done with matrix? |
| -------------- | ------------------------ |
| Rotation       | ✅ yes                    |
| Scaling        | ✅ yes                    |
| Translation    | ❌ no (needs addition)    |

**Problem:** Translation can’t be represented as a matrix, so combining all transformations is tricky.

**Solution:** Homogeneous coordinates allow us to:

- Represent all transformations (rotation, scaling, translation) **as matrix operations**  
- Combine multiple transformations easily  
- Handle **perspective transformations** in 3D graphics  

> In short: we go from **3D → 4D** in calculations, not to change the geometry, but to **simplify math and unify operations**.

---

## 🔹 Representation

A point in the projective plane is represented as a **triple**:

```

(X, Y, Z)

```

called its **homogeneous coordinates**, where `X`, `Y`, and `Z` are **not all zero**.

### Key properties

1. Multiplying all coordinates by a **non-zero scalar** does not change the point:

```

(X, Y, Z) ≡ (λX, λY, λZ), λ ≠ 0

```

2. Conversion to **Euclidean coordinates**:

- If `Z ≠ 0`:

```

(X, Y, Z) → (X/Z, Y/Z)

```

- If `Z = 0`:

```

(X, Y, 0) → point at infinity (direction of a line)

```

3. The **triple (0,0,0)** is undefined — it does not represent any point.  

4. The **origin** of the Euclidean plane is:

```

(0, 0, 1)

```

---

## 🔹 Intuition for points at infinity

- Points where `Z = 0` represent **directions** rather than positions.  
- Parallel lines share the same **point at infinity** in the direction they are pointing.  
- This allows **all lines to intersect exactly once** in projective geometry, even parallel ones.

---

## 🔹 Example: Using Homogeneous Coordinates for 2D Transformation

Suppose we have a point in 2D Cartesian coordinates:

$$
P = (2, 3)
$$

We want to **translate** it by $(dx, dy) = (5, 4)$.

### 1️⃣ Cartesian approach

Translation is **not a matrix operation** in normal Cartesian coordinates:

$$
P' = P + (dx, dy) = (2+5, 3+4) = (7, 7)
$$

---

### 2️⃣ Homogeneous coordinates approach

Convert the point to **homogeneous coordinates**:

$$
P_h = 
\begin{bmatrix}
X \\
Y \\
Z
\end{bmatrix}
=
\begin{bmatrix}
2 \\
3 \\
1
\end{bmatrix}
$$

Now, we can represent **translation** as a matrix:

$$
T = 
\begin{bmatrix}
1 & 0 & dx \\
0 & 1 & dy \\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 5 \\
0 & 1 & 4 \\
0 & 0 & 1
\end{bmatrix}
$$

---

### 3️⃣ Apply transformation

Multiply the translation matrix by the homogeneous point:

$$
P'_h = T \cdot P_h
=
\begin{bmatrix}
1 & 0 & 5 \\
0 & 1 & 4 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\
3 \\
1
\end{bmatrix}
=
\begin{bmatrix}
1\cdot 2 + 0\cdot 3 + 5\cdot 1 \\
0\cdot 2 + 1\cdot 3 + 4\cdot 1 \\
0\cdot 2 + 0\cdot 3 + 1\cdot 1
\end{bmatrix}
=
\begin{bmatrix}
7 \\
7 \\
1
\end{bmatrix}
$$

---

### 4️⃣ Back to Cartesian coordinates

Divide by $Z = 1$ to return to normal 2D coordinates:

$$
P' = (X/Z, Y/Z) = (7, 7)
$$

Translation is now a **matrix operation**, fully compatible with rotation, scaling, and perspective.

---

## 🔹 Why this is powerful

- We can **combine multiple transformations** (rotation, scaling, translation) into a single matrix.  
- Homogeneous coordinates allow **everything to be matrix math**, which is ideal for graphics programming and computer vision.

---

## 🔹 Summary

Homogeneous coordinates are:

- A **3-component representation** of 2D points (or 4-component for 3D)  
- A tool to **unify transformations** in computer graphics  
- Essential for handling **translation, rotation, scaling, and perspective** with matrices  
- Capable of representing **points at infinity**, giving projective geometry its powerful properties


# 2 — Camera Parameters: Extrinsic vs Intrinsic

**Definition:**  
A camera projection can be viewed as two consecutive transformations:

1. **Extrinsic transformation** — converts points from the **world coordinate system** to the **camera coordinate system**.
    
2. **Intrinsic transformation** — converts points from the **camera coordinate system** to **image pixel coordinates**.
    

Together, they describe how a 3D point in the world becomes a 2D point in an image.

---

## 🔹 The Big Picture

The camera projection process can be visualized as:

```text
World Coordinates
        ↓
 Extrinsic Parameters
        ↓
Camera Coordinates
        ↓
 Intrinsic Parameters
        ↓
 Image Pixels
```

Each step answers a different question:

- **Extrinsics:** Where is the camera and where is it looking?
    
- **Intrinsics:** How does the camera map 3D points onto its image sensor?
    

---

# 🔹 Extrinsic Parameters

## What are they?

Extrinsic parameters describe the **position and orientation of the camera in the world**.

They answer:

> "Where is the camera located, and how is it rotated?"

Their purpose is to transform a point from **world coordinates** into **camera coordinates**.

---

## Cartesian Representation

Suppose we have a 3D point in the world:

$$  
X_w =  
\begin{bmatrix}  
X_w \  
Y_w \  
Z_w  
\end{bmatrix}  
$$

To express this point relative to the camera, we apply:

$$  
X_c = RX_w + t  
$$

where:

$$  
R =  
\begin{bmatrix}  
r_{11} & r_{12} & r_{13}\  
r_{21} & r_{22} & r_{23}\  
r_{31} & r_{32} & r_{33}  
\end{bmatrix}  
$$

is the rotation matrix, and

$$  
t =  
\begin{bmatrix}  
t_x\  
t_y\  
t_z  
\end{bmatrix}  
$$

is the translation vector.

---

### Why this is Cartesian

This equation is expressed in Cartesian coordinates because:

- Points have only three coordinates ((X,Y,Z))
    
- Translation is added separately
    
- The transformation is not a single matrix multiplication
    

---

## Homogeneous Representation

To combine rotation and translation into one matrix operation, we use homogeneous coordinates.

The world point becomes:

$$  
X_w =  
\begin{bmatrix}  
X_w\  
Y_w\  
Z_w\  
1  
\end{bmatrix}  
$$

The transformation becomes:

$$  
X_c =  
\begin{bmatrix}  
R & t\  
0 & 1  
\end{bmatrix}  
X_w  
$$

where

$$  
\begin{bmatrix}  
R & t\  
0 & 1  
\end{bmatrix}  
$$

is called the **extrinsic matrix**.

---

## Why this is useful

Using homogeneous coordinates allows us to:

- Represent rotation and translation with a single matrix
    
- Chain multiple transformations together
    
- Keep all transformations as matrix multiplications
    

> In short: the extrinsic matrix tells us where the camera is and where it is looking.

---

# 🔹 Intrinsic Parameters

## What are they?

Intrinsic parameters describe the **internal properties of the camera**.

They answer:

> "Given a point relative to the camera, where does it appear in the image?"

Their purpose is to transform a point from **camera coordinates** into **image coordinates**.

---

## Cartesian Representation

Suppose a point is already expressed in camera coordinates:

$$  
X_c =  
\begin{bmatrix}  
X_c\  
Y_c\  
Z_c  
\end{bmatrix}  
$$

Using the pinhole camera model, the point projects onto the image plane as:

$$  
x = f_x \frac{X_c}{Z_c} + c_x  
$$

$$  
y = f_y \frac{Y_c}{Z_c} + c_y  
$$

where:

- (f_x) and (f_y) are the focal lengths in pixel units
    
- (c_x) and (c_y) are the coordinates of the principal point
    

---

### Why this is Cartesian

This equation is expressed in Cartesian coordinates because:

- It contains a division by (Z_c)
    
- The projection is described directly using coordinates
    
- No matrix representation is used yet
    

---

## Homogeneous Representation

The intrinsic parameters can be grouped into a matrix:

$$  
K =  
\begin{bmatrix}  
f_x & 0 & c_x\  
0 & f_y & c_y\  
0 & 0 & 1  
\end{bmatrix}  
$$

called the **intrinsic matrix**.

Projection becomes:

$$  
p = KX_c  
$$

where:

$$  
p =  
\begin{bmatrix}  
u\  
v\  
w  
\end{bmatrix}  
$$

is the projected point in homogeneous image coordinates.

---

## Back to Pixel Coordinates

To recover the actual image coordinates, divide by (w):

$$  
x = \frac{u}{w}  
$$

$$  
y = \frac{v}{w}  
$$

This is exactly the same idea used when converting homogeneous coordinates back to Euclidean coordinates.

---

## Why this is useful

Using the intrinsic matrix allows us to:

- Represent projection as matrix multiplication
    
- Encode focal length and image center in a compact form
    
- Combine projection with other camera transformations
    

> In short: the intrinsic matrix tells us how the camera converts 3D rays into image pixels.

---

# 🔹 Combining Extrinsics and Intrinsics

The complete camera projection process is:

1. Convert the world point into camera coordinates using the extrinsic matrix.
    
2. Convert the camera coordinates into image coordinates using the intrinsic matrix.
    

This gives the famous camera projection equation:

$$  
p \sim K[R|t]X_w  
$$

where:

- (X_w) = world point
    
- ([R|t]) = extrinsic parameters
    
- (K) = intrinsic parameters
    
- (p) = image point
    

---

## 🔹 Summary

### Extrinsic Parameters

- Describe the camera pose in the world
    
- Transform:
    

$$  
\text{World Coordinates}  
\rightarrow  
\text{Camera Coordinates}  
$$

- Cartesian form:
    

$$  
X_c = RX_w + t  
$$

- Homogeneous form:
    

$$  
X_c =  
\begin{bmatrix}  
R & t\  
0 & 1  
\end{bmatrix}  
X_w  
$$

---

### Intrinsic Parameters

- Describe the camera optics and sensor geometry
    
- Transform:
    

$$  
\text{Camera Coordinates}  
\rightarrow  
\text{Image Coordinates}  
$$

- Cartesian form:
    

$$  
x = f_x \frac{X_c}{Z_c} + c_x  
$$

$$  
y = f_y \frac{Y_c}{Z_c} + c_y  
$$

- Homogeneous form:
    

$$  
p = KX_c  
$$

with

$$  
K =  
\begin{bmatrix}  
f_x & 0 & c_x\  
0 & f_y & c_y\  
0 & 0 & 1  
\end{bmatrix}  
$$

---

### Full Camera Model

$$  
p \sim K[R|t]X_w  
$$

This equation is the foundation of classical computer vision and camera geometry.