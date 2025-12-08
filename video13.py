from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video13(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)
        title = Tex("Wave Transformations", stroke_width=2).set_color_by_gradient(RED, GREEN, BLUE)
        titleSR = always_redraw(lambda: SurroundingRectangle(title, color=YELLOW, buff=0.2).move_to(title.get_center()))

        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/8],
            y_range=[-2, 2, 1],
            tips=False,
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        amp = ValueTracker(1.00)
        periodicity = ValueTracker(1.00)
        xshift = ValueTracker(0.00)
        yshift = ValueTracker(0.00)

        sine = axes.plot(lambda x: amp.get_value()*np.sin(periodicity.get_value()*(x - xshift.get_value())) + yshift.get_value()).set_color_by_gradient([RED, GREEN, BLUE])
        sineLabel = MathTex(r"a"+r"\sin("+r"k"+r"("+r"x"+r"-"+r"c"+r"))+"+r"d", substrings_to_isolate=[r"a", r"k", r"c", r"d"], stroke_width=2).next_to(axes, UP)
        sineLabel[0].set_color(PURE_RED)
        sineLabel[2].set_color(PURE_GREEN)
        sineLabel[4].set_color(BLUE)
        sineLabel[6].set_color(PINK)

        setting = Tex("Amplitude", color=PURE_RED, stroke_width=2).scale(0.85).next_to(axes, DOWN*0.75)

        ampLabel = always_redraw(lambda: MathTex(fr"a={round(amp.get_value(), 2):>5}", color=PURE_RED, stroke_width=2).move_to([-3, -3.5, 0]))
        periodicityLabel = always_redraw(lambda: MathTex(fr"k={round(periodicity.get_value(), 2):>5}", color=PURE_GREEN, stroke_width=2).move_to([-1, -3.5, 0]))
        xshiftLabel = always_redraw(lambda: MathTex(fr"c={round(xshift.get_value(), 2):>5}", color=BLUE, stroke_width=2).move_to([1, -3.5, 0]))
        yshiftLabel = always_redraw(lambda: MathTex(fr"d={round(yshift.get_value(), 2):>5}", color=PINK, stroke_width=2).move_to([3, -3.5, 0]))

        labels = VGroup(ampLabel, periodicityLabel, yshiftLabel, xshiftLabel)

        self.play(Create(title))
        self.play(Create(titleSR))

        titleSR.clear_updaters()
        titleSR.add_updater(lambda sr: sr.move_to(title.get_center()))

        self.play(Uncreate(titleSR), title.animate.shift(UP*4))

        titleSR.clear_updaters()

        self.play(Create(axes), Create(sine), Create(sineLabel), Write(ampLabel), Write(periodicityLabel), Write(yshiftLabel), Write(xshiftLabel))

        sine.add_updater(lambda f: f.become(axes.plot(lambda x: amp.get_value()*np.sin(periodicity.get_value()*(x - xshift.get_value())) + yshift.get_value()).set_color_by_gradient([RED, GREEN, BLUE])))

        self.wait(0.5)
        self.play(SpinInFromNothing(setting))
        self.wait(0.5)
        aSR = SurroundingRectangle(sineLabel[0], color=YELLOW, buff=0.1)
        ampSR = always_redraw(lambda: SurroundingRectangle(ampLabel, color=YELLOW, buff=0.2, stroke_width=6))

        aLine = always_redraw(lambda: DashedLine(
            start=axes.c2p(xshift.get_value()+PI/(2*abs(periodicity.get_value())), yshift.get_value()),
            end=axes.c2p(xshift.get_value()+PI/(2*abs(periodicity.get_value())), amp.get_value()*np.sin(periodicity.get_value()*(xshift.get_value()+PI/(2*abs(periodicity.get_value()))-xshift.get_value()))+yshift.get_value()),
            color=PURE_RED
        ))

        aLineLabel= always_redraw(lambda: MathTex(r"a", color=PURE_RED, stroke_width=2).scale(0.75).next_to(aLine, RIGHT*0.35))

        aLabSR = always_redraw(lambda: SurroundingRectangle(aLineLabel, color=YELLOW, buff=0.2))

        aLine2 = always_redraw(lambda: DashedLine(
            start=axes.c2p(xshift.get_value()-PI/(2*abs(periodicity.get_value())), yshift.get_value()),
            end=axes.c2p(xshift.get_value()-PI/(2*abs(periodicity.get_value())), amp.get_value()*np.sin(periodicity.get_value()*(xshift.get_value()-PI/(2*abs(periodicity.get_value()))-xshift.get_value()))+yshift.get_value()),
            color=PURE_RED
        ))

        aLineLabel2= always_redraw(lambda: MathTex(r"a", color=PURE_RED, stroke_width=2).scale(0.75).next_to(aLine2, RIGHT*0.35))

        aLabSR2 = always_redraw(lambda: SurroundingRectangle(aLineLabel2, color=YELLOW, buff=0.1))
        
        self.play(Create(aSR), Create(ampSR), Create(aLine), Create(aLineLabel), Create(aLine2), Create(aLineLabel2), run_time=1)
        self.play(ReplacementTransform(aSR, aLabSR), ReplacementTransform(ampSR.copy(), aLabSR), ReplacementTransform(aSR.copy(), aLabSR2), ReplacementTransform(ampSR.copy(), aLabSR2), run_time=1)
        self.play(FadeOut(aLabSR), FadeOut(aLabSR2))
        self.play(amp.animate.set_value(2.00))
        self.play(amp.animate.set_value(-1.00))
        self.play(amp.animate.set_value(1))
        self.wait(0.5)

        kSR = SurroundingRectangle(sineLabel[2], color=YELLOW, buff=0.1)
        periodicitySR = always_redraw(lambda: SurroundingRectangle(periodicityLabel, buff=0.2, stroke_width=6))

        kLineTEMPLATE = always_redraw(lambda: DashedLine(
            start=axes.c2p(xshift.get_value()+PI/abs(periodicity.get_value()), amp.get_value()+yshift.get_value()),
            end=axes.c2p(xshift.get_value()-PI/abs(periodicity.get_value()), amp.get_value()+yshift.get_value()),
            color=PURE_GREEN
        ).set_opacity(0))

        kLbound = always_redraw(lambda: DashedLine(
            start=axes.c2p(xshift.get_value()+PI/abs(periodicity.get_value()), 0),
            end=axes.c2p(xshift.get_value()+PI/abs(periodicity.get_value()), amp.get_value()+yshift.get_value()),
            color=PURE_GREEN
        ))

        kRbound = always_redraw(lambda: DashedLine(
            start=axes.c2p(xshift.get_value()-PI/abs(periodicity.get_value()), 0),
            end=axes.c2p(xshift.get_value()-PI/abs(periodicity.get_value()), amp.get_value()+yshift.get_value()),
            color=PURE_GREEN
        ))
        
        kLine = always_redraw(lambda: Brace(
            mobject=kLineTEMPLATE,
            direction=UP,
            color=PURE_GREEN
        ))

        kLineLabel= always_redraw(lambda: MathTex(r"\frac{2\pi}{|k|}", color=PURE_GREEN, stroke_width=2).scale(0.75).next_to(kLine, UP*0.35))

        kLabSR = always_redraw(lambda: SurroundingRectangle(kLineLabel, color=YELLOW, buff=0.1))

        self.play(setting.animate.become(Tex("Periodicity", color=PURE_GREEN, stroke_width=2).scale(0.85).next_to(axes, DOWN*0.75)), FadeOut(aLineLabel), FadeOut(aLineLabel2), FadeOut(aLine), FadeOut(aLine2), ReplacementTransform(ampSR, periodicitySR), run_time=1)
        self.add(kLineTEMPLATE.set_opacity(0))
        self.play(Create(kSR), Create(kLine), Create(kLineLabel), Create(kLbound), Create(kRbound), run_time=1)
        self.play(ReplacementTransform(kSR, kLabSR), ReplacementTransform(periodicitySR.copy(), kLabSR))
        self.play(FadeOut(kLabSR))
        self.play(periodicity.animate.set_value(3.00))
        self.play(periodicity.animate.set_value(1/2))
        self.play(periodicity.animate.set_value(1.00))
        self.wait(0.5)

        cSR = SurroundingRectangle(sineLabel[4], color=YELLOW, buff=0.2)
        xshiftSR = always_redraw(lambda: SurroundingRectangle(xshiftLabel, color=YELLOW, buff=0.1, stroke_width=6))
        dSR = SurroundingRectangle(sineLabel[6], color=YELLOW, buff=0.2)
        yshiftSR = always_redraw(lambda: SurroundingRectangle(yshiftLabel, color=YELLOW, buff=0.1, stroke_width=6))

        cLine = always_redraw(lambda: Line(
            start=axes.c2p(0, 0),
            end=axes.c2p(xshift.get_value(), 0),
            color=BLUE,
            stroke_width=8
        ))
        dLine = always_redraw(lambda: Line(
            start=axes.c2p(0, 0),
            end=axes.c2p(0, yshift.get_value()),
            color=PINK,
            stroke_width=8
        ))

        cLineLabel= always_redraw(lambda: MathTex(r"c", color=BLUE, stroke_width=2).scale(0.75).next_to(cLine.get_end(), UL*0.35))
        dLineLabel= always_redraw(lambda: MathTex(r"d", color=PINK, stroke_width=2).scale(0.75).next_to(dLine.get_end(), DR*0.35))

        cLabSR = always_redraw(lambda: SurroundingRectangle(cLineLabel, color=YELLOW, buff=0.2, stroke_width=8))
        dLabSR = SurroundingRectangle(dLineLabel, color=YELLOW, buff=0.2, stroke_width=8)

        self.play(setting.animate.become(Tex("Phase Shift", color=BLUE, stroke_width=2).scale(0.85).next_to(axes, DOWN*0.75)), FadeOut(kLineLabel), FadeOut(kLineTEMPLATE), FadeOut(kLine), FadeOut(kLbound), FadeOut(kRbound), ReplacementTransform(periodicitySR, xshiftSR), run_time=1)
        self.play(Create(cSR), Create(cLine), Create(cLineLabel), run_time=1)
        self.play(ReplacementTransform(cSR, cLabSR), ReplacementTransform(xshiftSR.copy(), cLabSR), run_time=1)
        self.play(FadeOut(cLabSR))
        self.play(xshift.animate.set_value(2.00), run_time=1)
        self.play(xshift.animate.set_value(-2.00), run_time=1)
        self.play(xshift.animate.set_value(0), run_time=1)
        self.wait(0.5)

        self.play(setting.animate.become(Tex("Vertical Shift", color=PINK, stroke_width=2).scale(0.85).next_to(axes, DOWN*0.75)), FadeOut(cLineLabel), FadeOut(cLine), ReplacementTransform(xshiftSR, yshiftSR), run_time=1)
        self.play(Create(dSR), Create(dLine), Create(dLineLabel), run_time=1)
        self.play(ReplacementTransform(dSR, dLabSR), ReplacementTransform(yshiftSR.copy(), dLabSR), run_time=1)
        self.play(FadeOut(dLabSR))
        self.play(yshift.animate.set_value(1))
        self.play(yshift.animate.set_value(-1))
        self.play(yshift.animate.set_value(0))
        self.wait(0.5)

        labelSR = always_redraw(lambda: SurroundingRectangle(labels, color=YELLOW, buff=0.2, stroke_width=6))

        cNew = always_redraw(lambda: DashedLine(
            start=axes.c2p(xshift.get_value(), 0),
            end=axes.c2p(xshift.get_value(), yshift.get_value()),
            color=BLUE
        ))
        
        dNew = always_redraw(lambda: DashedLine(
            start=axes.c2p(0, yshift.get_value()),
            end=axes.c2p(xshift.get_value(), yshift.get_value()),
            color=PINK
        ))

        newLBL = always_redraw(lambda: MathTex(r"(c, d)").scale(0.75).set_color_by_gradient(BLUE, PINK).next_to(axes.c2p(xshift.get_value(), yshift.get_value()), UR))
        newLBLSR = always_redraw(lambda: SurroundingRectangle(newLBL, buff=0.2, color=YELLOW))

        cSR = SurroundingRectangle(sineLabel[4], color=YELLOW, buff=0.2)
        dSR = SurroundingRectangle(sineLabel[6], color=YELLOW, buff=0.2)

        self.play(
            setting.animate.become(Tex("Horizontal + Vertical Shift", stroke_width=2).set_color_by_gradient(RED, GREEN, BLUE).scale(0.85).next_to(axes, DOWN*0.75)),
            FadeOut(dLineLabel),
            FadeOut(dLine),
            Create(cNew), Create(dNew), Create(newLBL),
            Create(labelSR),
            ReplacementTransform(xshiftSR, newLBLSR), ReplacementTransform(yshiftSR, newLBLSR), ReplacementTransform(dSR, newLBLSR), ReplacementTransform(cSR, newLBLSR),
            run_time=1
        )
        self.play(FadeOut(newLBLSR))
        self.play(xshift.animate.set_value(1), yshift.animate.set_value(1), run_time=1)
        self.play(xshift.animate.set_value(1), yshift.animate.set_value(-1), run_time=1)
        self.play(xshift.animate.set_value(-1), yshift.animate.set_value(1), run_time=1)
        self.play(xshift.animate.set_value(-2), yshift.animate.set_value(-2), run_time=1)
        self.play(xshift.animate.set_value(0), yshift.animate.set_value(0), run_time=1)
        self.wait(1)
        self.play(FadeOut(*[m for m in self.mobjects if m is not sineLabel]), FadeOut(sine))
        self.play(sineLabel.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(FadeOut(sineLabel))

# manim -pqh video13.py video13