from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video14(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Integrals Explained").set_color_by_gradient(BLUE, WHITE)
        titleSR = always_redraw(lambda: SurroundingRectangle(title, color=YELLOW, buff=0.2).move_to(title.get_center()))

        self.play(Write(title), Create(titleSR), run_time=1)

        titleSR.clear_updaters()
        titleSR.add_updater(lambda SR: SR.become(SurroundingRectangle(title, color=YELLOW, buff=0.2).move_to(title.get_center())))

        self.play(title.animate.shift(UP*3), Uncreate(titleSR))
        self.wait(0.5)

        axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 5, 1],
            tips=False,
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )

        graph = axes.plot(lambda x: 0.9*x*np.sin(0.8*(x-1.1))+0.9).set_color_by_gradient([BLUE, WHITE])

        lowerbound = always_redraw(lambda: DashedLine(
            start=axes.c2p(1, 0),
            end=axes.c2p(1, 0.9*1*np.sin(0.8*(1-1.1))+0.9)
        ).set_color_by_gradient([BLUE, WHITE]))

        a = MathTex("a").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(axes.c2p(1, -0.5))
        b = MathTex("b").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(axes.c2p(3, -0.5))

        upperbound = always_redraw(lambda: DashedLine(
            start=axes.c2p(3, 0),
            end=axes.c2p(3, 0.9*3*np.sin(0.8*(3-1.1))+0.9)
        ).set_color_by_gradient([BLUE, WHITE]))

        region = axes.get_area(
            graph,
            x_range=[1, 3],
            opacity=0.25,
        ).set_color_by_gradient([BLUE, WHITE])

        regionLabel = Tex("What is the area?").scale(0.65).set_color_by_gradient(BLUE, WHITE).move_to([region.get_center()[0], region.get_center()[1]-1, 0])

        fx = MathTex("f(x)").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(axes.c2p(2.5, 3.85))

        div = ValueTracker(1)

        self.play(Create(axes), Create(graph), Write(fx))
        self.play(Create(lowerbound), Create(upperbound), Write(a), Write(b))
        self.play(FadeIn(region), Write(regionLabel))
        self.wait(1)
        self.play(regionLabel.animate.become(MathTex("A").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to([region.get_center()[0], region.get_center()[1]-0.75, 0])))

        Areaequals = MathTex("Area=").scale(0.9).set_color_by_gradient(BLUE, WHITE).shift(DOWN*5)
        IAEquals = always_redraw(lambda: MathTex("I = Area=").scale(0.9).set_color_by_gradient(BLUE, WHITE).shift(DOWN*5+LEFT*0.25))

        regionSmall = region.copy().scale(0.25).next_to(Areaequals, RIGHT)
        
        self.play(ReplacementTransform(regionLabel, Areaequals), Create(regionSmall))

        riemanns1 = always_redraw(lambda: axes.get_riemann_rectangles(
            graph,
            x_range=[1, 3],
            dx=div.get_value(),
            input_sample_type="left",
            blend=True,
            fill_opacity=0.5
        ).set_color_by_gradient([BLUE, WHITE]))

        fxi = Line(
            start=axes.c2p(1, 0),
            end=axes.c2p(1, axes.p2c(riemanns1[-2].get_corner(UL))[1]),
            color=YELLOW
        )

        fxiLabel = MathTex("f(x_{i})", color=YELLOW).scale(0.9).next_to(fxi, LEFT)

        fxi2 = Line(
            start=axes.c2p(3, 0),
            end=axes.c2p(3, axes.p2c(riemanns1[-1].get_corner(UR))[1]),
            color=YELLOW
        )

        fxiLabel2 = MathTex("f(x_{i})", color=YELLOW).scale(0.9).next_to(fxi2, RIGHT)

        deltax = Line(
            start=axes.c2p(1, 0),
            end=axes.c2p(2, 0),
            color=YELLOW
        )

        deltaxLabel = MathTex("\\Delta x", color=YELLOW).scale(0.9).next_to(deltax, DOWN)

        deltax2 = Line(
            start=axes.c2p(2, 0),
            end=axes.c2p(3, 0),
            color=YELLOW
        )

        deltaxLabel2 = MathTex("\\Delta x", color=YELLOW).scale(0.9).next_to(deltax2, DOWN)

        self.play(Write(riemanns1), FadeOut(region))
        self.play(Create(fxi), Write(fxiLabel), Create(fxi2), Write(fxiLabel2), Create(deltax), Write(deltaxLabel), Create(deltax2), Write(deltaxLabel2))

        rect1 = riemanns1[-1].copy().set_fill(color=YELLOW, opacity=0.15)
        rect1area = MathTex("f(x_{i})\\cdot\\Delta x", color=YELLOW).scale(0.5).move_to(rect1.get_center())
        rect2 = riemanns1[-2].copy().set_fill(color=YELLOW, opacity=0.15)
        rect2area = MathTex("f(x_{i})\\cdot\\Delta x", color=YELLOW).scale(0.5).move_to(rect2.get_center())

        self.play(Create(rect1), Create(rect2))
        self.play(Write(rect1area), Write(rect2area))

        Iequals = MathTex("I=f(x_i)\\Delta x + f(x_i)\\Delta x").scale(0.9).set_color_by_gradient(BLUE, WHITE).next_to(Areaequals, UP*2.5)
        Isum = always_redraw(lambda: MathTex("I=\\sum_{i=1}^"+f"\\infty"+" f(x_i)\\Delta x", substrings_to_isolate=["\\infty"]).scale(0.9).set_color_by_gradient(BLUE, WHITE).next_to(Areaequals, UP*2.5) if math.floor(2/div.get_value()) >= 10 else MathTex("I=\\sum_{i=1}^"+f"{math.floor(2/div.get_value())}"+" f(x_i)\\Delta x", substrings_to_isolate=[f"{math.floor(2/div.get_value())}"]).scale(0.9).set_color_by_gradient(BLUE, WHITE).next_to(Areaequals, UP*2.5))

        Isum_1 = MathTex("I=\\sum_{i=1}^"+f"\\infty"+" f(x_i)\\Delta x", substrings_to_isolate=["\\infty"]).scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(Isum.get_center())

        self.play(ReplacementTransform(rect1area, Iequals), ReplacementTransform(rect2area, Iequals))
        self.wait(0.5)
        self.play(ReplacementTransform(Iequals, Isum), ReplacementTransform(Areaequals, IAEquals))
        self.remove(rect1, rect2, Iequals)
        self.play(FadeOut(deltax), FadeOut(deltaxLabel), FadeOut(deltax2), FadeOut(deltaxLabel2),
                  FadeOut(fxi), FadeOut(fxiLabel), FadeOut(fxi2), FadeOut(fxiLabel2))
        
        iter = 1/2
        count = 1
        while div.get_value() != 1*iter**10:
            self.play(div.animate.set_value(div.get_value()*iter**10), run_time=2/count)
            count += 1

        finaleq = MathTex("\\int_a^b f(x) dx").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(ORIGIN)

        self.wait(0.5)
        self.play(FadeOut(*[m for m in self.mobjects if m is not Isum]))
        self.remove(Isum)
        self.remove(Isum_1)
        self.play(Isum_1.animate.move_to(ORIGIN))
        self.wait(0.5)
        self.play(ReplacementTransform(Isum_1, finaleq))

        self.wait(2)
        self.play(FadeOut(finaleq))

# manim -pqh video14.py video14