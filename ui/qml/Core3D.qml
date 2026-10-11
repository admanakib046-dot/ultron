import QtQuick
import QtQuick3D
import QtQuick3D.Helpers

// ============================================================================
// Core3D.qml - "Ultron core" wireframe hologram
// ----------------------------------------------------------------------------
// Matches the movie-prop reference: a dense, woven, gold/amber wireframe
// sphere built from many great-circle rings at scattered random tilts, so the
// rings overlap into a "cage" silhouette rather than reading as separate flat
// orbits. Built entirely from built-in QtQuick3D primitives (#Sphere,
// #Cylinder, #Cube) - no external models, no textures, no placeholders.
//
// RENDERING NOTE: almost every piece is OPAQUE with a strong emissiveFactor.
// QtQuick3D's View3D has no order-independent transparency, so stacking many
// overlapping alphaMode:Blend objects causes visible sorting artifacts (hard
// edges, objects popping through each other). Only one or two large, simple
// translucent shells are used here, and they never overlap one another.
//
// Contains:
//   - Transparent background (drop straight into any dashboard)
//   - Dense woven wireframe cage: 12 great-circle rings at scattered random
//     tilts, each built from small bright opaque segments
//   - Warm white-gold core glowing through the gaps in the cage
//   - A few radiating filament sparks
//   - Sparse orbiting motes outside the cage
//   - Subtle animated scan ring
//   - Subtle energy pulse shockwave
//   - Sparse background starfield
//   - Multiple PointLights (warm gold) + DirectionalLight
//   - PerspectiveCamera with slow cinematic idle motion
//   - ExtendedSceneEnvironment bloom / glow (where supported)
//
// Drop-in component, ~700x700.
// ============================================================================

Item {
    id: root
    width: 700
    height: 700

    View3D {
        id: view3d
        anchors.fill: parent
        camera: camera   // FIX: View3D never had an active camera assigned.

        environment: ExtendedSceneEnvironment {
            id: sceneEnv
            backgroundMode: SceneEnvironment.Transparent
            antialiasingMode: SceneEnvironment.MSAA
            antialiasingQuality: SceneEnvironment.High

            // Bloom tuned moderately - the reference image shows individual
            // wire strands clearly, so glow must not be so strong it washes
            // the whole cage into one blob.
            glowEnabled: true
            glowIntensity: 3.5
            glowBloom: 1.2
            glowStrength: 5.0
            glowQualityHigh: true
            glowUseBicubicUpscale: true
            glowHDRMinimumValue: 1.0
            glowHDRMaximumValue: 16.0
            glowHDRScale: 2.0

            tonemapMode: SceneEnvironment.TonemapModeLinear

            vignetteEnabled: true
            vignetteStrength: 0.4
            vignetteColor: Qt.rgba(0.02, 0.01, 0.0, 1)
        }

        // ------------------------------------------------------------------
        // Camera - gentle cinematic idle sway
        // ------------------------------------------------------------------
        Node {
            id: cameraRig
            SequentialAnimation on eulerRotation.y {
                loops: Animation.Infinite
                NumberAnimation { from: -8; to: 8; duration: 10000; easing.type: Easing.InOutSine }
                NumberAnimation { from: 8; to: -8; duration: 10000; easing.type: Easing.InOutSine }
            }

            PerspectiveCamera {
                id: camera
                position: Qt.vector3d(0, 0, 470)
                clipNear: 1
                clipFar: 6000
                fieldOfView: 36

                SequentialAnimation on position {
                    loops: Animation.Infinite
                    PropertyAnimation { to: Qt.vector3d(0, 15, 450); duration: 7000; easing.type: Easing.InOutSine }
                    PropertyAnimation { to: Qt.vector3d(0, -10, 470); duration: 7000; easing.type: Easing.InOutSine }
                }
            }
        }

        // ------------------------------------------------------------------
        // WORLD ROOT - everything below (lights, starfield, reactor) is
        // nested inside this single node. Its scale auto-shrinks to fit
        // whatever space the component actually gets, so if the host
        // dashboard gives this component a non-square area (e.g. a wide,
        // short panel), the whole scene shrinks to fit inside the smaller
        // dimension instead of being cropped top/bottom or left/right.
        // The component was designed at a 700x700 baseline, so fitScale
        // is 1.0 at 700x700 and shrinks proportionally below that.
        // ------------------------------------------------------------------
        Node {
            id: worldRoot
            property real fitScale: Math.max(0.001, Math.min(view3d.width, view3d.height) / 700)
            scale: Qt.vector3d(fitScale, fitScale, fitScale)

        // ------------------------------------------------------------------
        // Lighting rig - warm gold, matching the reference photo's palette
        // ------------------------------------------------------------------
        DirectionalLight {
            eulerRotation: Qt.vector3d(-45, 35, 0)
            color: "#fff0d0"
            brightness: 1.3
        }

        PointLight {
            position: Qt.vector3d(-260, 140, -180)
            color: "#ffb648"
            brightness: 8
            quadraticFade: 3.0
        }

        PointLight {
            position: Qt.vector3d(200, -180, 220)
            color: "#ff8c2e"
            brightness: 5
            quadraticFade: 4.0
        }

        // Core light - the reactor itself acting as a light source.
        PointLight {
            id: coreLight
            position: Qt.vector3d(0, 0, 0)
            color: "#fff2d6"
            brightness: 220
            quadraticFade: 2.0
            SequentialAnimation on brightness {
                loops: Animation.Infinite
                NumberAnimation { from: 180; to: 260; duration: 1600; easing.type: Easing.InOutQuad }
                NumberAnimation { from: 260; to: 180; duration: 1600; easing.type: Easing.InOutQuad }
            }
        }

        // ====================================================================
        // BACKGROUND STARFIELD - sparse, small, opaque, far away.
        // ====================================================================
        Node {
            Repeater3D {
                model: 50
                Model {
                    id: starModel
                    required property int index
                    property real seedA: index * 12.9898
                    property real seedB: index * 78.233
                    property real rx: (Math.sin(seedA) * 43758.5453) % 1.0
                    property real ry: (Math.sin(seedB) * 12543.789) % 1.0
                    property real rz: (Math.sin(seedA + seedB) * 5642.123) % 1.0

                    source: "#Sphere"
                    position: Qt.vector3d((rx - 0.5) * 2200, (ry - 0.5) * 1600, -600 - Math.abs(rz) * 1400)
                    scale: Qt.vector3d(0.02, 0.02, 0.02)
                    materials: PrincipledMaterial {
                        baseColor: "#ffe0a8"
                        emissiveFactor: Qt.vector3d(1.2, 1.0, 0.7)
                        lighting: PrincipledMaterial.NoLighting
                    }
                }
            }
        }

        // ====================================================================
        // REACTOR ROOT
        // ====================================================================
        Node {
            id: reactorRoot

            SequentialAnimation on eulerRotation.y {
                loops: Animation.Infinite
                NumberAnimation { from: 0; to: 360; duration: 130000 }
            }

            // ----------------------------------------------------------------
            // 1) CORE - warm white-gold center glowing through the cage gaps.
            //    Opaque + emissive; the halo is the only blended layer here.
            // ----------------------------------------------------------------
            Model {
                id: innerCore
                source: "#Sphere"
                scale: Qt.vector3d(0.3, 0.3, 0.3)
                materials: PrincipledMaterial {
                    baseColor: "#ffffff"
                    emissiveFactor: Qt.vector3d(120, 110, 90)
                    lighting: PrincipledMaterial.NoLighting
                }
                SequentialAnimation on scale {
                    loops: Animation.Infinite
                    PropertyAnimation { to: Qt.vector3d(0.35, 0.35, 0.35); duration: 1400; easing.type: Easing.InOutQuad }
                    PropertyAnimation { to: Qt.vector3d(0.26, 0.26, 0.26); duration: 1400; easing.type: Easing.InOutQuad }
                }
            }

            Model {
                id: coreHalo
                source: "#Sphere"
                scale: Qt.vector3d(0.5, 0.5, 0.5)
                materials: PrincipledMaterial {
                    baseColor: "#ffb559"
                    emissiveFactor: Qt.vector3d(25, 18, 10)
                    opacity: 0.65
                    alphaMode: PrincipledMaterial.Blend
                    lighting: PrincipledMaterial.NoLighting
                }
                SequentialAnimation on opacity {
                    loops: Animation.Infinite
                    NumberAnimation { from: 0.28; to: 0.45; duration: 1800; easing.type: Easing.InOutSine }
                    NumberAnimation { from: 0.45; to: 0.28; duration: 1800; easing.type: Easing.InOutSine }
                }
            }

            // ----------------------------------------------------------------
            // 2) WOVEN WIREFRAME CAGE - the main feature. Many great-circle
            //    rings, each at a scattered pseudo-random tilt, so together
            //    they overlap into a dense sphere-shaped cage of light, like
            //    the reference image. Every segment is opaque (no blend), so
            //    there is nothing here for the renderer to sort incorrectly.
            // ----------------------------------------------------------------
            Repeater3D {
                id: cageRepeater
                model: 12

                Node {
                    id: ringNode
                    required property int index

                    // Scattered pseudo-random orientation per ring so the
                    // rings don't line up into neat concentric shells - they
                    // criss-cross like a hand-wound wire ball.
                    property real seedA: index * 37.219 + 4.1
                    property real seedB: index * 91.345 + 7.7
                    property real rndX: (Math.sin(seedA) * 43758.5453) % 1.0
                    property real rndZ: (Math.sin(seedB) * 12543.789) % 1.0

                    property real cageRadius: 235 + ((index % 3) * 8)
                    property int segCount: 34

                    eulerRotation: Qt.vector3d(rndX * 180, 0, rndZ * 180)

                    SequentialAnimation on eulerRotation.y {
                        loops: Animation.Infinite
                        NumberAnimation {
                            from: index % 2 === 0 ? 0 : 360
                            to: index % 2 === 0 ? 360 : 0
                            duration: 26000 + index * 3500
                        }
                    }

                    Repeater3D {
                        model: ringNode.segCount
                        Model {
                            id: segModel
                            required property int index
                            property real segAngle: (index / ringNode.segCount) * 2 * Math.PI
                            // Every 6th segment is a brighter "solder joint" spark,
                            // matching the bright node points visible in the
                            // reference wireframe.
                            property bool isSpark: index % 6 === 0

                            source: "#Sphere"
                            position: Qt.vector3d(
                                ringNode.cageRadius * Math.cos(segAngle),
                                0,
                                ringNode.cageRadius * Math.sin(segAngle)
                            )
                            scale: isSpark ? Qt.vector3d(0.8, 0.8, 0.8) : Qt.vector3d(0.6, 0.6, 0.6)

                            materials: PrincipledMaterial {
                                baseColor: isSpark ? "#fff0c0" : "#ffb04d"
                                emissiveFactor: isSpark ? Qt.vector3d(6, 4.5, 2) : Qt.vector3d(3.2, 2, 0.6)
                                lighting: PrincipledMaterial.NoLighting
                            }
                        }
                    }
                }
            }

            // ----------------------------------------------------------------
            // 3) RADIATING FILAMENT SPARKS - a few thin bright threads from
            //    near the core out toward the cage surface.
            // ----------------------------------------------------------------
            Repeater3D {
                model: 7
                Model {
                    id: filamentModel
                    required property int index
                    property real fSeedA: index * 51.17 + 2.3
                    property real fSeedB: index * 27.53 + 8.9
                    property real fRndX: (Math.sin(fSeedA) * 43758.5453) % 1.0
                    property real fRndZ: (Math.sin(fSeedB) * 12543.789) % 1.0

                    source: "#Cube"
                    eulerRotation: Qt.vector3d(fRndX * 360, 0, fRndZ * 360)
                    scale: Qt.vector3d(0.008, 1.6 + fRndX, 0.008)
                    materials: PrincipledMaterial {
                        baseColor: "#ffe6b0"
                        emissiveFactor: Qt.vector3d(4, 3, 1.3)
                        lighting: PrincipledMaterial.NoLighting
                    }

                    SequentialAnimation on scale {
                        loops: Animation.Infinite
                        PropertyAnimation { to: Qt.vector3d(0.008, 2.0 + fRndX, 0.008); duration: 1300 + index * 200; easing.type: Easing.InOutSine }
                        PropertyAnimation { to: Qt.vector3d(0.008, 1.3 + fRndX, 0.008); duration: 1300 + index * 200; easing.type: Easing.InOutSine }
                    }
                }
            }

            // ----------------------------------------------------------------
            // 4) SPARSE OUTER MOTES - a few embers drifting just outside the
            //    cage, opaque, no trails.
            // ----------------------------------------------------------------
            Repeater3D {
                model: 5
                Node {
                    id: orbitNode
                    required property int index
                    property real orbitRadius: 320 + index * 26
                    property real orbitSpeed: 9000 + index * 1500

                    eulerRotation: Qt.vector3d((index * 41) % 90, 0, (index * 67) % 90)

                    SequentialAnimation on eulerRotation.y {
                        loops: Animation.Infinite
                        NumberAnimation {
                            from: 0
                            to: index % 2 === 0 ? 360 : -360
                            duration: orbitNode.orbitSpeed
                        }
                    }

                    Node {
                        position: Qt.vector3d(orbitNode.orbitRadius, 0, 0)
                        Model {
                            source: "#Sphere"
                            scale: Qt.vector3d(0.09, 0.09, 0.09)
                            materials: PrincipledMaterial {
                                baseColor: "#ffcf7a"
                                emissiveFactor: Qt.vector3d(3.5, 2.5, 1)
                                lighting: PrincipledMaterial.NoLighting
                            }
                        }
                    }
                }
            }

            // ----------------------------------------------------------------
            // 5) SUBTLE SCAN RING - kept understated so it doesn't compete
            //    with the wireframe cage.
            // ----------------------------------------------------------------
            Model {
                id: scanRing
                source: "#Cylinder"
                scale: Qt.vector3d(1.75, 0.006, 1.75)
                materials: PrincipledMaterial {
                    baseColor: "#ffdb96"
                    emissiveFactor: Qt.vector3d(2.5, 1.8, 0.7)
                    opacity: 0.35
                    alphaMode: PrincipledMaterial.Blend
                    lighting: PrincipledMaterial.NoLighting
                }
                SequentialAnimation on position {
                    loops: Animation.Infinite
                    PropertyAnimation { to: Qt.vector3d(0, 200, 0); duration: 3000; easing.type: Easing.InOutSine }
                    PropertyAnimation { to: Qt.vector3d(0, -200, 0); duration: 3000; easing.type: Easing.InOutSine }
                }
                SequentialAnimation on eulerRotation.y {
                    loops: Animation.Infinite
                    NumberAnimation { from: 0; to: 360; duration: 7000 }
                }
            }

            // ----------------------------------------------------------------
            // 6) SUBTLE ENERGY PULSE - single translucent shockwave, fades
            //    fully each cycle so it never persistently overlaps the halo.
            // ----------------------------------------------------------------
            Model {
                id: energyPulse
                source: "#Sphere"
                scale: Qt.vector3d(0.4, 0.4, 0.4)
                materials: PrincipledMaterial {
                    id: pulseMaterial
                    baseColor: "#ffe6b0"
                    opacity: 0.0
                    alphaMode: PrincipledMaterial.Blend
                    emissiveFactor: Qt.vector3d(2.5, 1.8, 0.8)
                    lighting: PrincipledMaterial.NoLighting
                }
                SequentialAnimation {
                    loops: Animation.Infinite
                    running: true
                    ParallelAnimation {
                        PropertyAnimation { target: energyPulse; property: "scale"; to: Qt.vector3d(2.4, 2.4, 2.4); duration: 2600; easing.type: Easing.OutCubic }
                        SequentialAnimation {
                            PropertyAnimation { target: pulseMaterial; property: "opacity"; to: 0.22; duration: 250 }
                            PropertyAnimation { target: pulseMaterial; property: "opacity"; to: 0.0; duration: 2350; easing.type: Easing.OutQuad }
                        }
                    }
                    PropertyAction { target: energyPulse; property: "scale"; value: Qt.vector3d(0.4, 0.4, 0.4) }
                    PauseAnimation { duration: 900 }
                }
            }
        } // reactorRoot
        } // worldRoot
    } // View3D
}
