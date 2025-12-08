from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video17(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Basic Math Functions").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2).add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        self.play(Write(title), Create(titleSR), run_time=1)
        self.play(title.animate.shift(UP*4), Uncreate(titleSR))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        
        g1 = VGroup(axes.plot(lambda x: x)).set_color_by_gradient(BLUE, WHITE)
        g1Label = MathTex(r"y = x").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g1UnderLabel = Tex("Linear").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        # Quadratic function with clipping
        def quad_clipped(x):
            y = x**2
            return np.clip(y, -5, 5)
        g2 = VGroup(axes.plot(quad_clipped, x_range=[-np.sqrt(5), np.sqrt(5)])).set_color_by_gradient([BLUE, WHITE])
        g2Label = MathTex(r"y = x^2").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g2UnderLabel = Tex("Quadratic").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        # Cubic function with clipping
        def cubic_clipped(x):
            y = x**3
            return np.clip(y, -5, 5)
        g3 = VGroup(axes.plot(cubic_clipped, x_range=[-np.cbrt(5), np.cbrt(5)])).set_color_by_gradient([BLUE, WHITE])
        g3Label = MathTex(r"y = x^3").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g3UnderLabel = Tex("Cubic").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g4 = VGroup(
            axes.plot(lambda x: 1/x, x_range=[-5, -0.2]),
            axes.plot(lambda x: 1/x, x_range=[0.2, 5])
        ).set_color_by_gradient([BLUE, WHITE])
        g4Label = MathTex(r"y = \frac{1}{x}").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g4UnderLabel = Tex("Reciprocal").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)
        
        g5 = VGroup(
            axes.plot(lambda x: 1/x**2, x_range=[-5, -1/np.sqrt(5)]),
            axes.plot(lambda x: 1/x**2, x_range=[1/np.sqrt(5), 5])
        ).set_color_by_gradient([BLUE, WHITE])
        g5Label = MathTex(r"y = \frac{1}{x^2}").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g5UnderLabel = Tex("Rational").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)
        
        g6 = VGroup(
            axes.plot(lambda x: np.e**x, x_range=[-5, np.log(5)])
        ).set_color_by_gradient([BLUE, WHITE])
        g6Label = MathTex(r"y = e^x").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g6UnderLabel = Tex("Exponential").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)
                
        g7 = VGroup(
            ParametricFunction(
                lambda t: axes.c2p(10**t, t),
                t_range=[-5, np.log10(5), 0.01]
            )
        ).set_color_by_gradient([BLUE, WHITE])
        g7Label = MathTex(r"y = \log (x)").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g7UnderLabel = Tex("Logarithmic").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g8 = VGroup(axes.plot(lambda x: 1)).set_color_by_gradient([BLUE, WHITE])
        g8Label = MathTex(r"y = 1").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g8UnderLabel = Tex("Constant").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g9 = VGroup(axes.plot(lambda x: abs(x))).set_color_by_gradient([BLUE, WHITE])
        g9Label = MathTex(r"y = |x|").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g9UnderLabel = Tex("Absolute Value").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g10 = VGroup(axes.plot(lambda x: np.sqrt(x), x_range=[0, 5])).set_color_by_gradient([BLUE, WHITE])
        g10Label = MathTex(r"y = \sqrt{x}").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g10UnderLabel = Tex("Square Root").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g11 = VGroup(axes.plot(lambda x: np.cbrt(x))).set_color_by_gradient([BLUE, WHITE])
        g11Label = MathTex(r"y = \sqrt[3]{x}").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g11UnderLabel = Tex("Cube Root").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g12 = VGroup(axes.plot(lambda x: np.sin(x))).set_color_by_gradient([BLUE, WHITE])
        g12Label = MathTex(r"y = \sin(x)").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g12UnderLabel = Tex("Sine").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        g13 = VGroup(axes.plot(lambda x: np.cos(x))).set_color_by_gradient([BLUE, WHITE])
        g13Label = MathTex(r"y = \cos(x)").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g13UnderLabel = Tex("Cosine").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        # Tangent with proper clipping - using numpy clip to limit y values
        def tan_clipped(x):
            return np.clip(np.tan(x), -5, 5)
        
        g14 = VGroup(
            axes.plot(tan_clipped, x_range=[-5, -3*np.pi/2 - 0.15], use_smoothing=False, discontinuities=[-3*np.pi/2]),
            axes.plot(tan_clipped, x_range=[-3*np.pi/2 + 0.15, -np.pi/2 - 0.15], use_smoothing=False, discontinuities=[-np.pi/2]),
            axes.plot(tan_clipped, x_range=[-np.pi/2 + 0.15, np.pi/2 - 0.15], use_smoothing=False, discontinuities=[np.pi/2]),
            axes.plot(tan_clipped, x_range=[np.pi/2 + 0.15, 3*np.pi/2 - 0.15], use_smoothing=False, discontinuities=[3*np.pi/2]),
            axes.plot(tan_clipped, x_range=[3*np.pi/2 + 0.15, 5], use_smoothing=False)
        ).set_color_by_gradient(BLUE, WHITE)
        g14Label = MathTex(r"y = \tan(x)").set_color_by_gradient(BLUE, WHITE).next_to(axes, UP)
        g14UnderLabel = Tex("Tangent").set_color_by_gradient(BLUE, WHITE).next_to(axes, DOWN)

        # Animations
        self.play(Create(axes))
        self.play(Write(g1Label), Create(g1), Write(g1UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g1Label, g2Label), FadeOut(g1), Create(g2),
                  TransformMatchingShapes(g1UnderLabel, g2UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g2Label, g3Label), FadeOut(g2), Create(g3),
                  TransformMatchingShapes(g2UnderLabel, g3UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g3Label, g4Label), FadeOut(g3), Create(g4),
                  TransformMatchingShapes(g3UnderLabel, g4UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g4Label, g5Label), FadeOut(g4), Create(g5),
                  TransformMatchingShapes(g4UnderLabel, g5UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g5Label, g6Label), FadeOut(g5), Create(g6),
                  TransformMatchingShapes(g5UnderLabel, g6UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g6Label, g7Label), FadeOut(g6), Create(g7),
                  TransformMatchingShapes(g6UnderLabel, g7UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g7Label, g8Label), FadeOut(g7), Create(g8),
                  TransformMatchingShapes(g7UnderLabel, g8UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g8Label, g9Label), FadeOut(g8), Create(g9),
                  TransformMatchingShapes(g8UnderLabel, g9UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g9Label, g10Label), FadeOut(g9), Create(g10),
                  TransformMatchingShapes(g9UnderLabel, g10UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g10Label, g11Label), FadeOut(g10), Create(g11),
                  TransformMatchingShapes(g10UnderLabel, g11UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g11Label, g12Label), FadeOut(g11), Create(g12),
                  TransformMatchingShapes(g11UnderLabel, g12UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g12Label, g13Label), FadeOut(g12), Create(g13),
                  TransformMatchingShapes(g12UnderLabel, g13UnderLabel))
        self.wait(0.75)
        self.play(TransformMatchingShapes(g13Label, g14Label), FadeOut(g13), Create(g14),
                  TransformMatchingShapes(g13UnderLabel, g14UnderLabel))
        self.wait(2)
        self.play(FadeOut(*[m for m in self.mobjects]))

# manim -pqh video17.py video17