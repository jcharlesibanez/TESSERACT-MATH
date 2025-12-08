from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video12(Scene):
    def construct(self):
        title = MathTex(r"\text{Taylor Series:}" + r"\sin (x)", substrings_to_isolate=[r"\sin (x)"]).set_color_by_gradient(BLUE, WHITE)
        title[1].set_color_by_gradient(RED, GREEN, BLUE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2)

        axes = Axes(
            x_range=[-4*PI+2*PI, 4*PI-2*PI, PI/8],
            y_range=[-2, 2, 1],
            tips=False,
            x_length=6.5,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )

        series1 = MathTex(r"\sin (x) \approx x", color=RED).next_to(axes, UP)
        series2 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!}", color=RED).next_to(axes, UP)
        series3 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!}", color=RED).next_to(axes, UP)
        series4 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}", color=RED).next_to(axes, UP)
        series5 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}\\ + \frac{x^9}{9!}", color=RED).next_to(axes, UP)
        series6 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}\\ + \frac{x^9}{9!} - \frac{x^{11}}{11!}", color=RED).next_to(axes, UP)
        series7 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}\\ + \frac{x^9}{9!} - \frac{x^{11}}{11!} + \frac{x^{13}}{13!}", color=RED).next_to(axes, UP)
        series8 = MathTex(r"\sin (x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}\\ + \frac{x^9}{9!} - \frac{x^{11}}{11!} + \frac{x^{13}}{13!} - \frac{x^{15}}{15!}", color=RED).next_to(axes, UP)

        finalseries = MathTex(r"\sin (x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!}x^{2n+1}").set_color_by_gradient(RED, GREEN, BLUE).next_to(axes, UP)

        s1 = axes.plot(lambda x: x, use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s2 = axes.plot(lambda x: x - x**(3)/math.factorial(3), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s3 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s4 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5) - x**(7)/math.factorial(7), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s5 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5) - x**(7)/math.factorial(7) + x**(9)/math.factorial(9), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s6 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5) - x**(7)/math.factorial(7) + x**(9)/math.factorial(9) - x**(11)/math.factorial(11), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s7 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5) - x**(7)/math.factorial(7) + x**(9)/math.factorial(9) - x**(11)/math.factorial(11) + x**(13)/math.factorial(13), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s8 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5) - x**(7)/math.factorial(7) + x**(9)/math.factorial(9) - x**(11)/math.factorial(11) + x**(13)/math.factorial(13) - x**(15)/math.factorial(15), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])
        s9 = axes.plot(lambda x: x - x**(3)/math.factorial(3) + x**(5)/math.factorial(5) - x**(7)/math.factorial(7) + x**(9)/math.factorial(9) - x**(11)/math.factorial(11) + x**(13)/math.factorial(13) - x**(15)/math.factorial(15) + x**(17)/math.factorial(17), use_smoothing=False).set_color_by_gradient([RED, GREEN, BLUE])

        rt = 0.5

        sin = axes.plot(lambda x: np.sin(x), use_smoothing=False, color=BLUE)
        sinL = MathTex(r"y=\sin (x)").next_to(axes, DOWN).set_color_by_gradient(RED, GREEN, BLUE)
        self.play(Write(title))
        self.play(Create(titleSR))
        self.play(FadeOut(title), FadeOut(titleSR))
        self.play(Create(axes), Create(sin), Create(sinL))
        self.wait(1)
        self.play(Create(series1), Create(s1))
        self.play(ReplacementTransform(series1, series2), ReplacementTransform(s1, s2), run_time=rt)
        self.play(ReplacementTransform(series2, series3), ReplacementTransform(s2, s3), run_time=rt)
        self.play(ReplacementTransform(series3, series4), ReplacementTransform(s3, s4), run_time=rt)
        self.play(ReplacementTransform(series4, series5), ReplacementTransform(s4, s5), run_time=rt)
        self.play(ReplacementTransform(series5, series6), ReplacementTransform(s5, s6), run_time=rt)
        self.play(ReplacementTransform(series6, series7), ReplacementTransform(s6, s7), run_time=rt)
        self.play(ReplacementTransform(series7, series8), ReplacementTransform(s7, s8), run_time=rt*2)
        self.wait(0.5)
        self.play(ReplacementTransform(series8, finalseries), ReplacementTransform(s8, s9), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(*[m for m in self.mobjects if m is not finalseries]))
        self.play(finalseries.animate.move_to(ORIGIN))
        finalseriesSR = SurroundingRectangle(finalseries, color=YELLOW, buff=0.2)
        self.play(Create(finalseriesSR))
        self.play(FadeOut(finalseries), FadeOut(finalseriesSR))

# manim -pqh video12.py video12