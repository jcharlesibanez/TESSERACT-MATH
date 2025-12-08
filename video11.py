from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video11(Scene):
    def construct(self):
        title = Tex("The Hyperbolic Functions").set_color_by_gradient(BLUE, WHITE)
        titleSr = SurroundingRectangle(title, color=YELLOW, buff=0.2).add_updater(lambda sr: sr.move_to(title.get_center()))
        self.play(Write(title), Create(titleSr), run_time=1)
        self.play(Uncreate(titleSr), title.animate.shift(UP*3.5))

        titleS = Tex("How did we discover them?").set_color_by_gradient(BLUE, PURE_GREEN, PURE_RED).scale(0.75).next_to(title, DOWN)

        xl = 6  
        yl = 6

        sin_ax = Axes(
            x_range=[-2*PI, 2*PI, PI/4],
            y_range=[-2, 2, 1],
            tips=True,
            x_length=xl,
            y_length=yl,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        sin = sin_ax.plot(lambda x: np.sin(x), use_smoothing=False, color=BLUE)
        sin_group = VGroup(sin_ax, sin)
        sin_group.scale(0.25).move_to(LEFT*2)
        sinL = MathTex(r"y=\sin (x)", color=BLUE).next_to(sin_ax, UP).scale(0.5)
        cos_ax = Axes(
            x_range=[-2*PI, 2*PI, PI/4],
            y_range=[-2, 2, 1],
            tips=True,
            x_length=xl,
            y_length=yl,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        cos = cos_ax.plot(lambda x: np.cos(x), use_smoothing=False, color=PURE_GREEN)
        cos_group = VGroup(cos_ax, cos)
        cos_group.scale(0.25)
        cosL = MathTex(r"y=\cos (x)", color=PURE_GREEN).next_to(cos_ax, UP).scale(0.5)
        pm = 0.35
        tan_ax = Axes(
            x_range=[-PI/2 + pm, PI/2 - pm, PI/8],
            y_range=[-2, 2, 1],
            tips=True,
            x_length=xl,
            y_length=yl,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        tan = tan_ax.plot(lambda x: np.tan(x), discontinuities=[-PI/2, PI/2], use_smoothing=False, color=PURE_RED)
        tan_group = VGroup(tan_ax, tan)
        tan_group.scale(0.25).move_to(RIGHT*2)
        tanL = MathTex(r"y=\tan (x)", color=PURE_RED).next_to(tan_ax, UP).scale(0.5)
#########################################################################################################################
        sinh_ax = Axes(
            x_range=[-math.sqrt(2)-0.8, math.sqrt(2)+0.8, PI/4],
            y_range=[-3, 3, 1],
            tips=True,
            x_length=xl,
            y_length=yl,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        sinh = sinh_ax.plot(lambda x: np.sinh(x), use_smoothing=False, color=BLUE)
        sinh_group = VGroup(sinh_ax, sinh)
        sinh_group.scale(0.25).move_to(LEFT*2+DOWN*2.25)
        sinhL = MathTex(r"y=\sinh (x)", color=BLUE).next_to(sinh_ax, UP).scale(0.5)
        cosh_ax = Axes(
            x_range=[-2, 2, PI/4],
            y_range=[-1, 4, 1],
            tips=True,
            x_length=xl,
            y_length=yl,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        cosh = cosh_ax.plot(lambda x: np.cosh(x), use_smoothing=False, color=PURE_GREEN)
        cosh_group = VGroup(cosh_ax, cosh)
        cosh_group.scale(0.25).move_to(DOWN*2.25)
        coshL = MathTex(r"y=\cosh (x)", color=PURE_GREEN).next_to(cosh_ax, UP).scale(0.5)
        tanh_ax = Axes(
            x_range=[-PI/2 + pm, PI/2 - pm, PI/8],
            y_range=[-2, 2, 1],
            tips=True,
            x_length=xl,
            y_length=yl,
            axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False},
        )
        tanh = tanh_ax.plot(lambda x: np.tanh(x), discontinuities=[-PI/2, PI/2], use_smoothing=False, color=PURE_RED)
        tanh_group = VGroup(tanh_ax, tanh)
        tanh_group.scale(0.25).move_to(RIGHT*2+DOWN*2.25)
        tanhL = MathTex(r"y=\tanh (x)", color=PURE_RED).next_to(tanh_ax, UP).scale(0.5)

        self.play(AnimationGroup(Create(sin_group), Write(sinL), Create(cos_group), Write(cosL), Create(tan_group), Write(tanL)), run_time=2)
        self.wait(0.25)
        self.play(AnimationGroup(Create(sinh_group), Write(sinhL), Create(cosh_group), Write(coshL), Create(tanh_group), Write(tanhL)), run_time=2)
        self.wait(0.25)
        self.play(GrowFromPoint(titleS, title.get_center()), run_time=1)
        self.wait(0.25)
        self.play(FadeOut(sin_group), FadeOut(cos_group), FadeOut(tan_group),
                  FadeOut(sinL), FadeOut(cosL), FadeOut(tanL), 
                  FadeOut(sinh_group), FadeOut(cosh_group), FadeOut(tanh_group),
                  FadeOut(sinhL), FadeOut(coshL), FadeOut(tanhL),
                  FadeOut(titleS),
                  run_time=0.5)
        
        r = 1.5

        angle = ValueTracker(PI/4)
        
        uc_ax = Axes(
            x_range=[-1.5, 1.5, 1],
            x_length=3,
            y_range=[-1.5, 1.5, 1],
            y_length=3,
            tips=False,
            x_axis_config={"include_numbers": False, "include_ticks": False},
            y_axis_config={"include_numbers": False, "include_ticks": False}
        )

        eqn1 = MathTex(r"x^2" + " + " + r"y^2 = 1", substrings_to_isolate=[" + "]).shift(UP*2.5).set_color_by_gradient(RED, WHITE)

        unit_circ = Circle(radius=r, color=RED)
        h_0 = Line(start=unit_circ.get_center(), end=[r, 0, 0], color=YELLOW)
        h = Line(start=unit_circ.get_center(), end=[r*np.cos(angle.get_value()), r*np.sin(angle.get_value()), 0], color=YELLOW)
        h.add_updater(lambda h: h.become(Line(start=unit_circ.get_center(), end=[r*np.cos(angle.get_value()), r*np.sin(angle.get_value()), 0], color=YELLOW)))
        theta = Angle(h_0, h, radius=0.25, color=YELLOW)
        theta.add_updater(lambda t: t.become(Angle(h_0, h, radius=0.25, color=YELLOW)))
        thetaL = MathTex(r"\theta", color=YELLOW).next_to([0.5*np.cos(angle.get_value()/2), 0.55*np.sin(angle.get_value()/2), 0], UP*0.2).scale(0.5)
        thetaL.add_updater(lambda tl: tl.become(MathTex(r"\theta", color=YELLOW).next_to([0.5*np.cos(angle.get_value()/2), 0.25*np.sin(angle.get_value()/2), 0], UP*0.2).scale(0.5)))

        yL = DashedLine(start=[0, r*np.sin(angle.get_value()), 0], end=[r*np.cos(angle.get_value()), r*np.sin(angle.get_value()), 0], color=PURE_GREEN)
        yLL = MathTex(r"\cos (\theta)", color=PURE_GREEN).next_to(yL, UP*0.15).scale(0.5)
        xL = DashedLine(start=[r*np.cos(angle.get_value()), 0, 0], end=[r*np.cos(angle.get_value()), r*np.sin(angle.get_value()), 0], color=BLUE)
        xLL = MathTex(r"\sin (\theta)", color= BLUE).scale(0.5).next_to(xL, RIGHT*0.15).rotate(3*PI/2)

        yL.add_updater(lambda y: y.become(DashedLine(start=[0, r*np.sin(angle.get_value()), 0], end=[r*np.cos(angle.get_value()), r*np.sin(angle.get_value()), 0], color=PURE_GREEN)))
        yLL.add_updater(lambda yy: yy.become(MathTex(r"\cos (\theta)", color= PURE_GREEN).next_to(yL, UP*0.05).scale(0.5)))
        xL.add_updater(lambda x: x.become(DashedLine(start=[r*np.cos(angle.get_value()), 0, 0], end=[r*np.cos(angle.get_value()), r*np.sin(angle.get_value()), 0], color=BLUE)))
        xLL.add_updater(lambda xx: xx.become(MathTex(r"\sin (\theta)", color= BLUE).scale(0.5).next_to(xL, RIGHT*0.05).rotate(3*PI/2)))

        self.play(Create(unit_circ), Create(h_0), Create(uc_ax), Write(eqn1))
        G = h_0.copy()
        self.play(Transform(G, h), Create(theta))
        self.remove(G)
        self.add(h)

        selTheta0 = MathTex(r"\theta = \frac{2\pi}{3}").shift(DOWN*2.5).set_color_by_gradient(YELLOW, WHITE).scale(0.75)
        selTheta1 = MathTex(r"\theta = \frac{\pi}{6}").shift(DOWN*2.5).set_color_by_gradient(YELLOW, WHITE).scale(0.75)
        selTheta2 = MathTex(r"\theta = \frac{\pi}{4}").shift(DOWN*2.5).set_color_by_gradient(YELLOW, WHITE).scale(0.75)

        identity1 = MathTex(r"\sin^2 (\theta) + \cos^2 (\theta) = 1").shift(DOWN*2.5).set_color_by_gradient(YELLOW, WHITE).scale(0.75)
        identity1Sr = SurroundingRectangle(identity1, color=YELLOW, buff=0.2)

        identity15 = MathTex(r"\sin^2 (\theta) + \cos^2 (\theta) "+ r"\neq" + r" 1", substrings_to_isolate=[r"\neq"]).shift(DOWN*2.5).set_color_by_gradient(RED, WHITE).scale(0.75)
        identity15Sr = SurroundingRectangle(identity15[1], color=YELLOW, buff=0.1)

        self.play(Create(thetaL), Create(yL), Create(xL), Write(yLL), Write(xLL), Write(selTheta0))
        self.wait(0.5)
        self.play(angle.animate.set_value(2*PI/3), ReplacementTransform(selTheta0, selTheta1), rate_func=smooth)
        self.play(angle.animate.set_value(PI/6), ReplacementTransform(selTheta1, selTheta2), rate_func=smooth)
        self.play(angle.animate.set_value(PI/4), ReplacementTransform(selTheta2, selTheta0), rate_func=smooth)
        self.wait(0.25)
        self.play(ReplacementTransform(selTheta0, identity1), Create(identity1Sr))
        self.play(Uncreate(identity1Sr))

        question = Tex("But what about for hyperbolas?").set_color_by_gradient(BLUE, WHITE).scale(0.75)

        minusToPlus = SurroundingRectangle(eqn1[1], color=YELLOW, buff=0.1)

        self.play(AnimationGroup(
            FadeOut(unit_circ),
            FadeOut(uc_ax),
            FadeOut(h_0),
            FadeOut(h),
            FadeOut(yL),
            FadeOut(yLL),
            FadeOut(xL),
            FadeOut(xLL),
            FadeOut(theta),
            FadeOut(thetaL),
            FadeOut(identity1)
        ))
        self.play(Write(question), run_time=1)
        self.wait(0.25)

        qToEqn = Arrow(start=[eqn1[1].get_center()[0], 0.5, 0], end=[eqn1[1].get_center()[0], 2, 0], color=BLUE, stroke_width=2)

        hyperbola = uc_ax.plot_parametric_curve(lambda x: np.array([0.5*np.cosh(x), 0.5*np.sinh(x)]), t_range=[-1.5,1.5], color=RED
        ).add(uc_ax.plot_parametric_curve(lambda x: np.array([-0.5*np.cosh(x), 0.5*np.sinh(x)]), t_range=[-1.5,1.5], color=RED))

        self.play(Create(qToEqn), Create(minusToPlus))
        self.play(ReplacementTransform(eqn1[1], MathTex(r" - ").shift(eqn1[1].get_center()).match_style(eqn1[1])), Uncreate(qToEqn), run_time=1)
        self.play(Uncreate(minusToPlus))
        self.wait(0.25)
        self.play(FadeOut(question), Create(uc_ax), Create(hyperbola))
        self.wait(0.25),
        self.play(Write(identity15), run_time=1)
        self.play(Create(identity15Sr))
        self.play(Uncreate(identity15Sr))
        self.wait(0.25)

        newfuncs = MathTex(
            r"\text{We need to invent new} \\ "
            r"\text{sine and cosine functions} \\ "
            r"\text{for hyperbolas.}"
        ).set_color_by_gradient(BLUE, WHITE).scale(0.65).next_to(identity15, DOWN)        
        newsin = MathTex(r"\sin"+r"h"+" (t) = ?", substrings_to_isolate=[r"h"]).set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(identity15, DOWN).shift(LEFT)
        newcos = MathTex(r"\cos"+r"h"+" (t) = ?", substrings_to_isolate=[r"h"]).set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(identity15, DOWN).shift(RIGHT)
        newsin[1].set_color(PURE_RED)
        newcos[1].set_color(PURE_RED)

        self.play(Write(newfuncs), run_time=1)
        self.wait(1)
        self.play(FadeOut(newfuncs))
        self.play(Write(newsin), Write(newcos))
        self.wait(0.25)
        self.play(
            newsin.animate.become(MathTex(r"\sinh (t) = ?").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(identity15, DOWN).shift(LEFT)),
            newcos.animate.become(MathTex(r"\cosh (t) = ?").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(identity15, DOWN).shift(RIGHT)))
        self.wait(1) 

        mustbetrue = MathTex(r"\text{To re-establish the identity, it must be true that:}").set_color_by_gradient(BLUE, WHITE).scale(0.75).shift(DOWN*2)
        dSinh = MathTex(r"\frac{d}{dt}\sinh (t) = \cosh (t)").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(identity15, DOWN)
        dCosh = MathTex(r"\frac{d}{dt}\cosh (t) = \sinh (t)").set_color_by_gradient(BLUE, WHITE).scale(0.75).next_to(identity15, DOWN*4.5)

        self.play(ReplacementTransform(identity15, mustbetrue), ReplacementTransform(newsin, dSinh), ReplacementTransform(newcos, dCosh))
        self.wait(2)

        rule = MathTex(r"\text{We know that:}\frac{d^2 f}{du^2}="+r"f(u)"+r".", substrings_to_isolate=[r"f(u)"]).set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).shift(DOWN*2)
        q = MathTex(r"\text{We want to find:}"+r"f(u).", substrings_to_isolate=[r"f(u)"]).set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(rule, DOWN)
        q[1].set_color(PURE_GREEN)

        tryexp = MathTex(r"\text{We try: }f(u)="+r"e^{ku}", substrings_to_isolate=[r"\text{We try: }f(u)="]).set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(rule, DOWN)
        deku1 = MathTex(r"\frac{d}{du}(e^{ku})=k\cdot e^{ku}").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(tryexp, DOWN)
        deku2 = MathTex(r"\frac{d^2}{du^2}(e^{ku})=k^{2}e^{ku}").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(tryexp, DOWN)
        deku3 = MathTex(r"k^{2}e^{ku}=e^{ku}").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(tryexp, DOWN)
        deku4 = MathTex(r"k^{2}=1").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(tryexp, DOWN)
        deku5 = MathTex(r"k=-1\text{ or }k=1").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(tryexp, DOWN)

        f_u = DashedLine(start=[1, 0, 0], end=[1, math.sqrt(3/4), 0], color=PURE_GREEN)
        f_uL = MathTex(r"f(u)", color=PURE_GREEN).next_to(f_u, RIGHT*0.1).scale(0.5)
        uLI = Line(start=[1,0,0], end=[1, math.sqrt(3/4), 0], color=PURE_BLUE)
        u = Polygon([0.5,0,0], [1, math.sqrt(3/4), 0], [1, 0, 0]).set_fill(PURE_BLUE).set_opacity(0.5)
        uL = MathTex(r"u", color=BLUE).move_to(u.get_center()).scale(0.5).shift(DOWN*0.2+RIGHT*0.05)

        self.play(FadeOut(mustbetrue), FadeOut(dSinh), FadeOut(dCosh))
        self.play(Write(rule))
        self.play(Write(q))
        self.wait(0.25)
        self.play(ReplacementTransform(q, tryexp), Create(f_u), Write(f_uL))
        self.play(Create(uLI), Create(u), Create(uL))
        self.wait(0.25)
        self.play(Create(deku1))
        self.wait(0.25)
        self.play(ReplacementTransform(deku1, deku2))
        self.wait(0.5)

        ruleSR = SurroundingRectangle(rule[1], color=YELLOW, buff=0.1)
        deku3SR = SurroundingRectangle(deku3, color=YELLOW, buff=0.1)

        self.play(Create(ruleSR))
        self.play(AnimationGroup(ReplacementTransform(ruleSR, deku3SR), ReplacementTransform(deku2, deku3)))
        self.play(Uncreate(deku3SR))
        self.wait(0.25)
        self.play(ReplacementTransform(deku3, deku4))
        self.wait(0.25)
        self.play(ReplacementTransform(deku4, deku5))
        self.wait(0.5)

        feq1 = MathTex(r"f(u)=e^u \text{ or } f(u)=e^{-u}").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).shift(DOWN*2)
        desc1 = MathTex(r"\text{Recall that }\sin(\theta) \text{ is even and }\cos(\theta) \text{ is odd.}").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(feq1, DOWN)
        desc2 = MathTex(r"\text{So:}").set_color_by_gradient(PURE_GREEN, WHITE).scale(0.75).next_to(feq1, DOWN)
        feq2 = MathTex(r"\sinh(x)=\frac{e^{x}-e^{-x}}{2}", color=BLUE).scale(0.75).next_to(desc1, DOWN)
        feq3 = MathTex(r"\cosh(x)=\frac{e^{x}+e^{-x}}{2}", color=PURE_GREEN).scale(0.75).next_to(feq2, DOWN)


        self.play(FadeOut(tryexp), FadeOut(deku5), FadeOut(rule), Write(feq1))
        self.wait(0.25)
        self.play(Write(desc1))
        self.wait(0.25)
        self.play(ReplacementTransform(feq1, feq2), Create(feq3), ReplacementTransform(desc1, desc2))
        self.wait(1)
        self.play(FadeOut(*[m for m in self.mobjects if m is not feq2 and m is not feq3]), feq2.animate.move_to(ORIGIN).shift(UP*1.5), feq3.animate.move_to(ORIGIN).shift(DOWN*1.5))

        feq4 = MathTex(r"\tanh(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}", color=PURE_RED).scale(0.75)
        feq4SR = SurroundingRectangle(feq4, color=YELLOW, buff=0.2)
        feq2SR = SurroundingRectangle(feq2, color=YELLOW, buff=0.2)
        feq3SR = SurroundingRectangle(feq3, color=YELLOW, buff=0.2)
        self.wait(0.25)

        self.play(Create(feq2SR), Create(feq3SR))
        self.play(Create(feq4), ReplacementTransform(feq2SR, feq4SR), ReplacementTransform(feq3SR, feq4SR))
        self.play(Uncreate(feq4SR))

        self.play(FadeOut(feq2), FadeOut(feq3), FadeOut(feq4))

# manim -pqh video11.py video11