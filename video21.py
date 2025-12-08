from manim import *
import numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video21(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Quadratic Equations").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2)
        self.play(Write(title), Create(titleSR), run_time=1)
        
        # Add updater AFTER creation
        titleSR.add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        
        self.play(title.animate.shift(UP*4), Uncreate(titleSR))
        empty = MathTex("")

        quadratic = MathTex("a"+"x^2+"+"b"+"x+"+"c", substrings_to_isolate=["a", "b", "c"]).shift(UP*3)
        quadratic[0].set_color(PURE_RED)
        quadratic[2].set_color(PURE_GREEN)
        quadratic[4].set_color(TEAL)
        
        self.play(TransformMatchingTex(empty, quadratic))
        self.wait(0.25)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
            x_length=4,
            y_length=4,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        ).scale(1.2).shift(DOWN*0.75)
        a, b, c = ValueTracker(1), ValueTracker(0), ValueTracker(0)

        asr = SurroundingRectangle(quadratic[0], color=YELLOW, buff=0.1)
        asrl = MathTex(f"a={a.get_value():<4.2f}", color=PURE_RED).scale(0.75).next_to(asr, DOWN).add_updater(lambda al: al.become(MathTex(f"a={a.get_value():<4.2f}", color=PURE_RED).scale(0.75).next_to(asr, DOWN)))
        bsr = SurroundingRectangle(quadratic[2], color=YELLOW, buff=0.1)
        bsrl = MathTex(f"b={b.get_value():<4.2f}", color=PURE_GREEN).scale(0.75).next_to(bsr, DOWN).add_updater(lambda bl: bl.become(MathTex(f"b={b.get_value():<4.2f}", color=PURE_GREEN).scale(0.75).next_to(bsr, DOWN)))
        csr = SurroundingRectangle(quadratic[4], color=YELLOW, buff=0.1)
        csrl = MathTex(f"c={c.get_value():<4.2f}", color=TEAL).scale(0.75).next_to(csr, DOWN).add_updater(lambda cl: cl.become(MathTex(f"c={c.get_value():<4.2f}", color=TEAL).scale(0.75).next_to(csr, DOWN)))

        def domain():
            A = a.get_value()
            B = b.get_value()
            C = c.get_value()

            D = B**2 - 4*A*(C - 5)

            # guard: no real intersections
            if D < 0 or A == 0:
                return [-5, 5, 0.01]  # fallback safe domain

            r1 = (-B - np.sqrt(D)) / (2*A)
            r2 = (-B + np.sqrt(D)) / (2*A)

            # ensure increasing order
            return [min(r1, r2), max(r1, r2), 0.01]


        qgraph = always_redraw(lambda: axes.plot(lambda x: a.get_value()*x**2+b.get_value()*x+c.get_value(), x_range=domain()).set_color_by_gradient([PURE_RED, PURE_BLUE, WHITE]))
        bfollows = axes.plot(lambda x: -x**2, x_range=domain(), color=GRAY).set_stroke(opacity=0.5)

        bdot = always_redraw(lambda: Dot(
            point=axes.c2p(-(b.get_value())/(2*a.get_value()), -(b.get_value()**2 -4*a.get_value()*c.get_value())/(4*a.get_value())),
            color=YELLOW,
            radius=0.05
        ))

        self.play(Create(axes), Create(qgraph))
        self.play(Create(asr), TransformMatchingShapes(empty, asrl))
        self.play(AnimationGroup(a.animate.set_value(3)))
        self.play(a.animate.set_value(0.2))
        self.play(AnimationGroup(a.animate.set_value(1)))
        self.play(TransformMatchingShapes(asrl, bsrl), ReplacementTransform(asr, bsr), FadeIn(bfollows, bdot))
        self.play(AnimationGroup(b.animate.set_value(4)))
        self.play(b.animate.set_value(-3))
        self.play(AnimationGroup(b.animate.set_value(0)))
        self.play(FadeOut(bfollows, bdot), ReplacementTransform(bsr, csr), TransformMatchingShapes(bsrl, csrl))
        self.play(AnimationGroup(c.animate.set_value(2)))
        self.play(c.animate.set_value(-2))
        self.play(AnimationGroup(c.animate.set_value(0)))
        self.play(FadeOut(csr), Uncreate(csrl))

        self.wait(0.25)

        QuadraticFormula = MathTex(r"x=\frac{-b\pm\sqrt{b^2 -4ac}}{2a}").set_color_by_gradient([PURE_BLUE, PURE_GREEN, WHITE]).scale(0.9)
        exampleproblem = Tex("Example problem").move_to(quadratic.get_center()).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        quadraticQ = MathTex("3"+"x^2-"+"18"+"x-"+"21", substrings_to_isolate=["3", "18", "21"]).set_color_by_gradient([WHITE, BLUE, WHITE]).shift(UP*1.75)

        self.play(FadeOut(axes, qgraph), FadeIn(QuadraticFormula))
        self.play(Circumscribe(QuadraticFormula), QuadraticFormula.animate.set_color_by_gradient(BLUE, WHITE))
        self.wait(0.25)
        self.play(ReplacementTransform(quadratic, quadraticQ), TransformMatchingTex(empty, exampleproblem))

        aL = MathTex("a", color=PURE_RED).scale(0.8).next_to(quadraticQ[0], DOWN*1.15)
        bL = MathTex("b", color=PURE_GREEN).scale(0.8).next_to(quadraticQ[2], DOWN)
        cL = MathTex("c", color=TEAL).scale(0.8).next_to(quadraticQ[4], DOWN*1.15)

        self.wait(0.25)
        self.play(FadeIn(aL, bL, cL))

        qf1 = MathTex(r"x=\frac{-b\pm\sqrt{b^2 -4(3)c}}{2(3)}").set_color_by_gradient(BLUE, WHITE).scale(0.9)
        qf2 = MathTex(r"x=\frac{-(-18)\pm\sqrt{(-18)^2 -4(3)c}}{2(3)}").set_color_by_gradient(BLUE, WHITE).scale(0.9)
        qf3 = MathTex(r"x=\frac{-(-18)\pm\sqrt{(-18)^2 -4(3)(-21)}}{2(3)}").set_color_by_gradient(BLUE, WHITE).scale(0.9)

        qf4 = MathTex(r"x=\frac{18\pm\sqrt{324+252}}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9)
        qf5 = MathTex(r"x=\frac{18\pm\sqrt{576}}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9)
        qf6 = MathTex(r"x=\frac{18\pm 24}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9)

        rf1 = MathTex(r"x=\frac{18+24}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(qf6.get_center(), RIGHT)
        rf2 = MathTex(r"x=\frac{18-24}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(qf6.get_center(), LEFT)
        rs1 = MathTex(r"x=\frac{42}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(qf6.get_center(), RIGHT)
        rs2 = MathTex(r"x=\frac{-6}{6}").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(qf6.get_center(), LEFT)
        rt1 = MathTex(r"x=7").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(qf6.get_center(), RIGHT)
        rt2 = MathTex(r"x=-1").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(qf6.get_center(), LEFT)

        self.play(TransformMatchingShapes(QuadraticFormula, qf1), Indicate(aL))
        self.wait(0.5)
        self.play(TransformMatchingShapes(qf1, qf2), Indicate(bL))
        self.wait(0.5)
        self.play(TransformMatchingShapes(qf2, qf3), Indicate(cL))
        self.wait(1)
        self.play(TransformMatchingShapes(qf3, qf4))
        self.wait(0.5)
        self.play(TransformMatchingShapes(qf4, qf5))
        self.wait(0.5)
        self.play(TransformMatchingShapes(qf5, qf6))
        self.wait(0.5)
        self.play(ReplacementTransform(qf6.copy(), rf1), ReplacementTransform(qf6, rf2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(rf1, rs1), TransformMatchingShapes(rf2, rs2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(rs1, rt1), TransformMatchingShapes(rs2, rt2))
        self.wait(0.5)
        self.play(Circumscribe(rt1), Circumscribe(rt2))

        axes2 = Axes(
            x_range=[-10, 10, 1],
            y_range=[-50, 50, 1],
            tips=False,
            x_length=4,
            y_length=4,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        ).shift(DOWN*2.5)
        qnew = always_redraw(lambda: axes2.plot(lambda x: 3*x**2-18*x-21, x_range=[-2.71, 8.71]).set_color_by_gradient([RED, WHITE]))
        self.play(Create(axes2), Create(qnew))

        ro1 = MathTex("(-1,0)", color=YELLOW).scale(0.65).move_to(axes2.c2p(-6, 5)).shift(UP)
        ro2 = MathTex("(7,0)", color=YELLOW).scale(0.65).move_to(axes2.c2p(4.5, 5)).shift(UP)
        
        root1Dot = Dot(
            point=axes2.c2p(-1,0),
            color=YELLOW,
            radius=0.05
        ).shift(UP)
        root2Dot = Dot(
            point=axes2.c2p(7,0),
            color=YELLOW,
            radius=0.05
        ).shift(UP)

        self.play(axes2.animate.shift(UP), ReplacementTransform(rt1, ro2), ReplacementTransform(rt2, ro1), Create(root1Dot), Create(root2Dot))

        quadratic = MathTex("a"+"x^2+"+"b"+"x+"+"c", substrings_to_isolate=["a", "b", "c"]).shift(UP)
        quadratic[0].set_color(PURE_RED)
        quadratic[2].set_color(PURE_GREEN)
        quadratic[4].set_color(TEAL)

        self.wait(1)
        self.play(FadeOut(*[m for m in self.mobjects if m is not QuadraticFormula and m is not quadratic]), Write(quadratic), Write(QuadraticFormula.shift(DOWN)))
        
        self.wait(2)
        self.play(FadeOut(*[m for m in self.mobjects]))

# manim -pqh video21.py video21