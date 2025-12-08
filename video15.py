from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video15(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Limits Explained").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2).add_updater(lambda SR: SR.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))

        self.play(Write(title), Create(titleSR), run_time=1)
        self.play(title.animate.shift(UP*3.5), Uncreate(titleSR))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
            x_length=5,
            y_length=5, 
            axis_config={"include_numbers": False, "include_ticks": False, "font_size": 0.25},
            y_axis_config={"include_numbers": True, "include_ticks": False},
        ).scale(0.8)

        graph = axes.plot(lambda x: np.cos(x)).set_color_by_gradient([BLUE, WHITE])
        graph2_1 = axes.plot(lambda x: x, x_range=[-5, 2]).set_color_by_gradient([BLUE, WHITE])
        graph2_2 = axes.plot(lambda x: x+2, x_range=[2, 5]).set_color_by_gradient([BLUE, WHITE])
        graph3 = axes.plot(lambda x: np.e**(-x), x_range=[-1.6, 5]).set_color_by_gradient([BLUE, WHITE])

        lim1 = MathTex(r"\lim_{x\to a} f(x)=").shift(DOWN*3).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        lim2 = MathTex(r"\lim_{x\to a} f(x)= "+r"1", substrings_to_isolate=[r"1"]).shift(DOWN*3).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        lim3 = MathTex(r"\lim_{x\to a} f(x)= "+r"DNE", substrings_to_isolate=[r"DNE"]).shift(DOWN*3).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        lim4 = MathTex(r"\lim_{x\to a} f(x)= "+r"0", substrings_to_isolate=[r"0"]).shift(DOWN*3).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        lim5 = MathTex(r"\lim_{x\to a} f(x)= "+r"\infty", substrings_to_isolate=[r"\infty"]).shift(DOWN*3).scale(0.9).set_color_by_gradient(BLUE, WHITE)

        lim2subSR = SurroundingRectangle(lim2[1], color=YELLOW, buff=0.1)
        lim3subSR = SurroundingRectangle(lim3[1], color=YELLOW, buff=0.1)
        lim4subSR = SurroundingRectangle(lim4[1], color=YELLOW, buff=0.1)
        lim5subSR = SurroundingRectangle(lim5[1], color=YELLOW, buff=0.1)

        aequals1 = MathTex(r"a=0").next_to(lim1, UP*0.5).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        aequals2 = MathTex(r"a=2").next_to(lim1, UP*0.5).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        aequals3_1 = MathTex(r"a=\infty").next_to(lim1, UP*0.5).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        aequals3_2 = MathTex(r"a=-\infty").next_to(lim1, UP*0.5).scale(0.9).set_color_by_gradient(BLUE, WHITE)

        xval = ValueTracker(PI)

        asx = MathTex(r"\text{as }x\to a").move_to(axes.c2p(-2.5, 2.5)).scale(0.8).set_color_by_gradient(BLUE, WHITE)
        yto = always_redraw(lambda: MathTex(fr"y \to "+fr"{np.cos(xval.get_value()):<5.2f}", substrings_to_isolate=[fr"{np.cos(xval.get_value()):<4.2f}"]).move_to(axes.c2p(2.5, 2.5)).scale(0.8).set_color_by_gradient(BLUE, WHITE))

        leftdot = always_redraw(lambda: Dot(
            point=axes.c2p(-xval.get_value(), np.cos(xval.get_value())),
            radius=0.1,
            color=YELLOW
        ))

        rightdot = always_redraw(lambda: Dot(
            point=axes.c2p(xval.get_value(), np.cos(xval.get_value())),
            radius=0.1,
            color=YELLOW
        ))

        ytosubSR = SurroundingRectangle(yto[1], color=YELLOW, buff=0.1)

        self.play(Create(axes), Create(graph), Write(lim1))
        self.play(Write(aequals1), Write(asx), Write(yto))
        self.play(Create(leftdot), Create(rightdot), Indicate(aequals1))
        self.play(xval.animate.set_value(0), rate_func=smootherstep, run_time=2)
        self.wait(0.1)
        self.play(Create(ytosubSR))
        self.play(ReplacementTransform(lim1, lim2), ReplacementTransform(ytosubSR, lim2subSR))

        self.wait(0.1)
        self.play(FadeOut(leftdot), FadeOut(rightdot), FadeOut(graph), FadeOut(lim2), FadeOut(lim2subSR), FadeOut(yto))

        a_dash = DashedLine(
            start=axes.c2p(2, 0),
            end=axes.c2p(2, 5)
        ).set_color_by_gradient([BLUE, WHITE])

        a_dashL = MathTex(r"a").scale(0.8).next_to(axes.c2p(2, 0), DOWN).set_color_by_gradient(BLUE, WHITE)

        xval.set_value(4)
        
        leftdot2 = always_redraw(lambda: Dot(
            point=axes.c2p(-(xval.get_value()-4), -xval.get_value()+4),
            radius=0.1,
            color=YELLOW
        ))

        rightdot2 = always_redraw(lambda: Dot(
            point=axes.c2p(xval.get_value(), abs(2+xval.get_value())),
            radius=0.1,
            color=YELLOW
        ))

        ytoright = always_redraw(lambda: MathTex(fr"a^+"+fr"{abs(2+xval.get_value()):>5.2f}", substrings_to_isolate=[fr"{xval.get_value()+2:>5.2f}"], color=YELLOW).next_to(rightdot2, UL*0.25).scale(0.65))
        ytoleft = always_redraw(lambda: MathTex(fr"a^-"+fr"{-xval.get_value()+4:>5.2f}", substrings_to_isolate=[fr"{xval.get_value():>5.2f}"], color=YELLOW).next_to(leftdot2, UR*0.25).scale(0.65))

        neq = MathTex(r"a^{-}\neq a^{+}").scale(0.65).next_to(title, DOWN).set_color_by_gradient(BLUE, WHITE)

        self.play(Create(graph2_1), Create(graph2_2), Write(lim1), ReplacementTransform(aequals1, aequals2), Create(a_dash), Write(a_dashL))
        self.play(Indicate(aequals2), Create(leftdot2), Create(rightdot2),
                  Create(ytoright), Create(ytoleft))
        self.play(xval.animate.set_value(2), rate_func=smootherstep, run_time=2)
        self.wait(0.1)
        amin = always_redraw(lambda: SurroundingRectangle(ytoleft, color=YELLOW, buff=0.1))
        aplus = always_redraw(lambda: SurroundingRectangle(ytoright, color=YELLOW, buff=0.1))

        neqSR = always_redraw(lambda: SurroundingRectangle(neq, color=YELLOW, buff=0.1))

        self.play(Create(amin), Create(aplus))
        self.play(Write(neq), ReplacementTransform(amin, neqSR), ReplacementTransform(aplus, neqSR))
        self.wait(0.25)
        self.play(ReplacementTransform(lim1, lim3), ReplacementTransform(neqSR, lim3subSR))
        self.remove(neqSR)
        self.wait(0.1)
        self.play(FadeOut(leftdot2), FadeOut(rightdot2), FadeOut(ytoleft), FadeOut(ytoright), FadeOut(graph2_1), FadeOut(graph2_2), FadeOut(lim3subSR), FadeOut(lim3), FadeOut(a_dash), FadeOut(a_dashL), FadeOut(neq))

        xval.set_value(0)

        rightdot3 = always_redraw(lambda: Dot(
            point=axes.c2p(xval.get_value(), np.e**(-xval.get_value())),
            radius=0.1,
            color=YELLOW
        ))

        ytoright2 = always_redraw(lambda: MathTex(fr"y={np.e**(-xval.get_value()):>5.2f}", color=YELLOW).next_to(rightdot3, UR*0.1).scale(0.8))
        lim1 = MathTex(r"\lim_{x\to a} f(x)=").shift(DOWN*3).scale(0.9).set_color_by_gradient(BLUE, WHITE)
        self.play(asx.animate.move_to(axes.c2p(-2.5, 1)), Create(graph3), Write(lim1), ReplacementTransform(aequals2, aequals3_1), Create(rightdot3), Create(ytoright2))
        self.wait(0.25)
        self.play(Indicate(aequals3_1))
        self.play(xval.animate.set_value(5), rate_func=smootherstep, run_time=2)

        # Remove old always_redraw and create new one
        self.remove(ytoright2)
        ytoright2 = always_redraw(lambda: MathTex(r"y\to 0", color=YELLOW).next_to(rightdot3, UR*0.1).scale(0.8))
        self.add(ytoright2)

        ytosubSR = always_redraw(lambda: SurroundingRectangle(
            MathTex(r"y\to 0", color=YELLOW).next_to(rightdot3, UR*0.1).scale(0.8), 
            color=YELLOW, buff=0.1
        ))
        self.play(Create(ytosubSR))
        self.play(ReplacementTransform(lim1, lim4), ReplacementTransform(ytosubSR, lim4subSR))
        self.play(FadeOut(lim4subSR))
        self.play(ReplacementTransform(aequals3_1, aequals3_2))
        self.play(Indicate(aequals3_2))

        # Remove old always_redraw and create new one
        self.remove(ytoright2)
        ytoright2 = always_redraw(lambda: MathTex(fr"y={np.e**(-xval.get_value()):>5.2f}", color=YELLOW).next_to(rightdot3, UR*0.1).scale(0.8))
        self.add(ytoright2)

        self.play(xval.animate.set_value(-1.6), rate_func=smootherstep, run_time=2)

        # Remove old always_redraw and create new one
        self.remove(ytoright2)
        ytoright2 = always_redraw(lambda: MathTex(r"y\to \infty", color=YELLOW).next_to(rightdot3, UR*0.1).scale(0.8))
        self.add(ytoright2)

        ytosubSR = always_redraw(lambda: SurroundingRectangle(
            MathTex(r"y\to \infty", color=YELLOW).next_to(rightdot3, UR*0.1).scale(0.8), 
            color=YELLOW, buff=0.1
        ))
        self.play(Create(ytosubSR))  # Add it to the scene first
        self.wait(0.1)  # Brief wait to let it render properly
        self.play(ReplacementTransform(lim4, lim5), ReplacementTransform(ytosubSR, lim5subSR))
        self.play(FadeOut(lim5subSR))
        self.remove(ytosubSR)  # Remove the original ytosubSR
        self.wait(1)
        self.play(FadeOut(*[m for m in self.mobjects]))

        self.wait(2)

# manim -pqh video15.py video15