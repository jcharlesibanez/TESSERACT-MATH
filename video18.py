from manim import *
import numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video18(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Mean Value Theorem").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2).add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        self.play(Write(title), Create(titleSR), run_time=1)
        self.play(title.animate.shift(UP*4), Uncreate(titleSR))

        theorem = MathTex(r"\text{Let }f\text{ be a continuous and differentiable function}").set_color_by_gradient(BLUE, WHITE).scale(0.8).shift(UP*3)
        theorem2 = MathTex(r"\text{Let }f\text{ be continuous on }[a, b]\text{ and differentiable on }(a,b).").set_color_by_gradient(BLUE, WHITE).scale(0.7).shift(UP*3)

        theorem3 = MathTex(r"\text{Then there exists a point }c\text{ in }(a,b) \text{ such that}").set_color_by_gradient(BLUE, WHITE).scale(0.65).shift(DOWN*3)
        theorem4 = MathTex(r"f'(c)"+" = "+r"\frac{f(b)-f(a)}{b-a}", substrings_to_isolate=[r"f'(c)", r"\frac{f(b)-f(a)}{b-a}"]).set_color_by_gradient(BLUE, WHITE).scale(0.8).next_to(theorem3, DOWN)

        axes = Axes(
            x_range=[-0.5, 5, 1],
            y_range=[-0.5, 5, 1],
            tips=False,
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )

        self.play(Create(axes), Write(theorem))

        f = axes.plot(lambda x: 0.9*x*np.sin(0.8*(x-1.1))+0.9).set_color_by_gradient([BLUE, WHITE])

        f2 = VGroup(
            axes.plot(lambda x: 0.9*x*np.sin(0.8*(x-1.1))+0.9, x_range=[-0.5, 1], stroke_opacity=0.25).set_color_by_gradient([BLUE, WHITE]),
            axes.plot(lambda x: 0.9*x*np.sin(0.8*(x-1.1))+0.9, x_range=[1, 4]).set_color_by_gradient([BLUE, WHITE]),
            axes.plot(lambda x: 0.9*x*np.sin(0.8*(x-1.1))+0.9, x_range=[4, 5], stroke_opacity=0.25).set_color_by_gradient([BLUE, WHITE])
        )

        self.play(Create(f))
        self.wait(0.25)
        self.play(TransformMatchingShapes(theorem, theorem2))
        self.wait(0.25)

        aLine = Line(
            start = axes.c2p(1, 0),
            end = axes.c2p(1, 5)
        )
        aLabel = MathTex("a").set_color_by_gradient(BLUE, WHITE).next_to(axes.c2p(1, 0), DOWN)

        bLine = Line(
            start = axes.c2p(4, 0),
            end = axes.c2p(4, 5)
        )
        bLabel = MathTex("b").set_color_by_gradient(BLUE, WHITE).next_to(axes.c2p(4, 0), DOWN)

        a = VGroup(aLine, aLabel)
        b = VGroup(bLine, bLabel)

        self.play(GrowFromPoint(a, axes.c2p(-0.5, 2.25)), GrowFromPoint(b, axes.c2p(5, 2.25)), TransformMatchingShapes(f, f2))
        self.wait(0.25)
        self.play(Write(theorem3))
        theorem4[2].set_color(YELLOW)
        self.play(Write(theorem4))
        self.wait(0.25)

        secantSR = SurroundingRectangle(theorem4[2], color=YELLOW, buff=0.1, stroke_width=8)
        secantLine = Line(  
            start=axes.c2p(1, 0.9*1*np.sin(0.8*(1-1.1))+0.9),
            end=axes.c2p(4, 0.9*4*np.sin(0.8*(4-1.1))+0.9),
            color=YELLOW,
            stroke_width=6
        )
        secantLineLabel = Tex("secant line", color=YELLOW).scale(0.8).move_to(secantLine.get_center()).rotate(
            float(
                np.arctan(
                    (
                        ((0.9*4*np.sin(0.8*(4-1.1))+0.9) -
                        (0.9*1*np.sin(0.8*(1-1.1))+0.9))
                        / (4 - 1)
                    )
                )
            )*(5/6)
        ).shift(DR*0.15)

        secantLineSR = SurroundingRectangle(secantLine, color=YELLOW, buff=0.1, stroke_width=8)

        self.play(Create(secantSR))
        self.play(ReplacementTransform(secantSR, secantLineSR))
        self.play(Create(secantLine), Create(secantLineLabel))
        self.play(FadeOut(secantLineSR))

        val = ValueTracker(1)

        c = MathTex(f"c={val.get_value():.2f}").set_color_by_gradient(BLUE, WHITE
                        ).scale(0.75).move_to(axes.c2p(2.5, 5)).add_updater(lambda s: s.become(MathTex(f"c={val.get_value():.2f}")).scale(0.75).set_color_by_gradient(BLUE, WHITE).move_to(axes.c2p(2.5, 5)))
        cslope = MathTex(fr"f'(c)={round(0.72 * round(val.get_value(), 2) * np.cos(0.8 * round(val.get_value(), 2) - 0.88) + 0.9 * np.sin(0.8 * round(val.get_value(), 2) - 0.88), 2)}"
                         ).scale(0.75).move_to(axes.c2p(2.5, 4.5)).add_updater(lambda s: s.become(MathTex(fr"f'(c)={round(0.72 * round(val.get_value(), 2) * np.cos(0.8 * round(val.get_value(), 2) - 0.88) + 0.9 * np.sin(0.8 * round(val.get_value(), 2) - 0.88), 2)}")).scale(0.75).set_color_by_gradient(BLUE, WHITE).move_to(axes.c2p(2.5, 4.5)))


        cDot = always_redraw(lambda: Dot(
            point=axes.c2p(val.get_value(), 0.9*val.get_value()*np.sin(0.8*(val.get_value()-1.1))+0.9),
            radius=0.1,
            color=BLUE
        ))

        cLine = always_redraw(
            lambda: next(iter([
                axes.plot(
                    lambda x: fc + fpc * (x - c),
                    color=BLUE,
                    stroke_width=6,
                    x_range=[1, 4]
                )
                for c in [val.get_value()]
                for fc in [0.9 * c * np.sin(0.8 * (c - 1.1)) + 0.9]
                for fpc in [0.72 * c * np.cos(0.8 * c - 0.88) + 0.9 * np.sin(0.8 * c - 0.88)]
            ]))
        )

        tangentLabel = always_redraw(
            lambda: next(iter([
                Tex("tangent line", color=BLUE).scale(0.8).move_to(axes.c2p(2.5, fc + fpc * (2.5 - c))).rotate(
                    float(np.arctan(fpc) * (5/6))
                ).shift(UL * 0.15)
                for c in [val.get_value()]
                for fc in [0.9 * c * np.sin(0.8 * (c - 1.1)) + 0.9]
                for fpc in [0.72 * c * np.cos(0.8 * c - 0.88) + 0.9 * np.sin(0.8 * c - 0.88)]
            ]))
        )

        clabels = VGroup(c, cslope)
        cLabelsSR = SurroundingRectangle(clabels, color=BLUE, buff=0.15, stroke_width=6)

        self.play(Write(c), Write(cslope), Create(cLabelsSR), Create(cDot), Create(cLine), Create(tangentLabel))
        self.wait(0.25)
        self.play(val.animate.set_value(3.062), run_time=2)
        self.wait(1)

        nonfadeouts = [theorem2, theorem3, theorem4]

        self.play(FadeOut(*[m for m in self.mobjects if m not in nonfadeouts]), FadeOut(c), FadeOut(cslope),
                  theorem2.animate.move_to(ORIGIN+UP*0.25),
                  theorem3.animate.move_to(ORIGIN+DOWN*0.25),
                  theorem4.animate.move_to(ORIGIN+DOWN))
        
        finaltheorem0 = MathTex(r"\text{If }f\mathrel{:} [a,b]\rightarrow \mathbb{R} \text{ is continuous on }[a, b]\text{ and differentiable on }(a,b),").set_color_by_gradient(BLUE, WHITE).scale(0.55).move_to(ORIGIN+UP*0.25)
        finaltheorem1 = MathTex(r"\text{then }\exists c \in (a,b) \text{ such that }f'(c)=\frac{f(b)-f(a)}{b-a}").set_color_by_gradient(BLUE, WHITE).scale(0.55).move_to(ORIGIN+DOWN*0.25)

        self.wait(0.5)
        self.play(TransformMatchingShapes(theorem2, finaltheorem0), TransformMatchingShapes(theorem3, finaltheorem1), FadeOut(theorem4))

        self.wait(2)

        self.play(FadeOut(*[m for m in self.mobjects]))

# manim -pqh video18.py video18