from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video10(MovingCameraScene):
    def construct(self):
        y_mod = -1.5

        CAR_BORDER = [
            [-2.72, 3.29+y_mod, 0],
            [-1.67, 3.7+y_mod, 0],
            [-0.22, 3.64+y_mod, 0],
            [1.04, 3.18+y_mod, 0],
            [2.41, 2.51+y_mod, 0],
            [2.604, 1.91+y_mod, 0],
            [2.8, 1.25+y_mod, 0],
            [2, 1.25+y_mod, 0],
            [1.85, 1.75+y_mod, 0],
            [1.25, 1.75+y_mod, 0],
            [1.15, 1.25+y_mod, 0],
            [-1.15, 1.25+y_mod, 0],
            [-1.35, 1.75+y_mod, 0],
            [-1.85, 1.75+y_mod, 0],
            [-2, 1.25+y_mod, 0],
            [-2.87, 1.26+y_mod, 0],
            [-2.88, 2.16+y_mod, 0],
        ]

        BACK_WINDOW_BORDER = [
            [-2.72, 3.29+y_mod, 0],
            [-1.67, 3.7+y_mod, 0],
            [-1.66, 3.1+y_mod, 0]
        ]

        MID_WINDOW_BORDER = [
            [-1.67, 3.7+y_mod, 0],
            [-1.66, 3.1+y_mod, 0],
            [0.16, 2.92+y_mod, 0],
            [-0.22, 3.64+y_mod, 0]
        ]

        FRONT_WINDOW_BORDER = [
            [-0.22, 3.64+y_mod, 0],
            [0.16, 2.92+y_mod, 0],
            [2.41, 2.51+y_mod, 0],
            [1.04, 3.18+y_mod, 0]
        ]

        IP1_BORDER = [
            [-2.72, 3.29+y_mod, 0],
            [-1.66, 3.1+y_mod, 0],
            [0.16, 2.92+y_mod, 0],
            [2.41, 2.51+y_mod, 0],
            [-2.07, 2.13+y_mod, 0]
        ]

        IP2_BORDER = [
            [-2.07, 2.13+y_mod, 0],
            [2.604, 1.91+y_mod, 0],
            [2.41, 2.51+y_mod, 0]
        ]

        CarFrame = Polygon(*CAR_BORDER, color=BLUE, stroke_width=2)
        BackWindow = Polygon(*BACK_WINDOW_BORDER, stroke_width=2).set_fill(DARK_BLUE, opacity=0.5)
        MidWindow = Polygon(*MID_WINDOW_BORDER, stroke_width=2).set_fill(DARK_BLUE, opacity=0.5)
        FrontWindow = Polygon(*FRONT_WINDOW_BORDER, stroke_width=2).set_fill(DARK_BLUE, opacity=0.5)

        ip1 = Polygon(*IP1_BORDER, color=BLUE, stroke_width=2).set_fill(BLUE, opacity=0.1)
        ip2 = Polygon(*IP2_BORDER, color=BLUE, stroke_width=2).set_fill(BLUE, opacity=0.1)

        SW = ValueTracker(2)

        BackWheel = Circle(radius=0.35, color=RED, stroke_width=SW.get_value()).move_to([-1.585, 1.25+y_mod//2, 0]).add_updater(lambda s: s.set_stroke(width=SW.get_value()))
        BackWheel_i = Circle(radius=0.125, color=RED, stroke_width=SW.get_value()).move_to(BackWheel.get_center()).add_updater(lambda s: s.set_stroke(width=SW.get_value()))

        FrontWheel = Circle(radius=0.35, color=RED, stroke_width=2).move_to([1.565, 1.25+y_mod//2, 0]).add_updater(lambda s: s.set_stroke(width=SW.get_value()))
        FrontWheel_i = Circle(radius=0.125, color=RED, stroke_width=2).move_to(FrontWheel.get_center()).add_updater(lambda s: s.set_stroke(width=SW.get_value()))

        Car = VGroup(CarFrame, BackWindow, MidWindow, FrontWindow, ip1, ip2)
        Car = Car.scale(0.65)

        Wheels = VGroup(BackWheel, FrontWheel, BackWheel_i, FrontWheel_i)
        Wheels = Wheels.scale(0.65)

        grass_set = VGroup([Line([i, 0.625+y_mod//2, 0], [i+0.2, 1+y_mod//2, 0], color=PURE_GREEN) for i in np.arange(-30, 30, 0.2)])

        title = Tex("Rotational Motion").set_color_by_gradient(BLUE, WHITE).move_to(Car.get_center()+UP*1.25).scale(0.75)
        title_SR = SurroundingRectangle(title, color=YELLOW, buff=0.1, stroke_width=2)

        mg_car = Arrow(start=[0, 1.25+y_mod//2, 0], end=[0, -1.25+y_mod//2, 0], color=PURE_GREEN, tip_length=0.25, stroke_width=3).add_updater(lambda o: self.bring_to_front(o))
        mg_label = MathTex("mg").scale(0.75).next_to(mg_car.get_center(), RIGHT)

        mg_car.add_updater(lambda g: g.move_to(Car.get_center()+DOWN*1.5))
        mg_label.add_updater(lambda g: g.next_to(mg_car.get_center(), RIGHT))

        Fn_car = Arrow(start=[0, 3.64+y_mod, 0], end=[0, 5.64+y_mod//2, 0], color=PURE_RED, tip_length=0.25, stroke_width=3).add_updater(lambda o: self.bring_to_front(o))
        Fn_label = MathTex(r"F_N").scale(0.75).next_to(Fn_car.get_center(), RIGHT)

        Fn_car.add_updater(lambda g: g.move_to(Car.get_center()+UP))
        Fn_label.add_updater(lambda g: g.next_to(Fn_car.get_center(), RIGHT))

        P = Dot(point=FrontWheel.get_center() + 0.35*0.65 * np.array([math.cos(self.time + PI/2)]), radius=0.01).set_color_by_gradient(BLUE, WHITE).add_updater(lambda o: self.bring_to_front(o))
        P.add_updater(lambda p: p.move_to(FrontWheel.get_center() + 0.35*0.65 * np.array([math.cos(self.time+PI/2), math.sin(self.time+PI/2), 0])))
        P_a = Arrow(start=P.get_center(),
                    end=P.get_center() + 0.2 * np.array([-math.sin(self.time+PI/2), math.cos(self.time+PI/2), 0]),
                    tip_length=0.04, stroke_width=0.5).set_color_by_gradient(BLUE, WHITE).add_updater(lambda o: self.bring_to_front(o))

        P_a.add_updater(
            lambda a: a.become(
                Arrow(start=P.get_center(),
                    end=P.get_center() + 0.2 * np.array([-math.sin(self.time+PI/2), math.cos(self.time+PI/2), 0]),
                    tip_length=0.04, stroke_width=0.5)
            )
        )
        P_a_label = MathTex(r"\vec{v}_P").scale(0.125).set_color_by_gradient(BLUE, WHITE).next_to(P_a.get_center(), UP*0.3).add_updater(lambda o: self.bring_to_front(o))
        P_a_label.add_updater(lambda p: p.next_to(P_a.get_center(), RIGHT*0.2))

        P_label = MathTex(r"P").scale(0.125).set_color_by_gradient(BLUE, WHITE).next_to(P.get_center(), RIGHT*0.2).add_updater(lambda o: self.bring_to_front(o))
        P_label.add_updater(lambda p: p.next_to(P.get_center(), RIGHT*0.2))

        Pa_SR = SurroundingRectangle(P_a, color=YELLOW, buff=0.025, stroke_width=0.5).add_updater(lambda r: r.become(SurroundingRectangle(P_a, color=YELLOW, buff=0.025, stroke_width=0.5)))

        R_line = Line(start=FrontWheel.get_center(), end=FrontWheel.get_center()+RIGHT*0.2275, color=RED, stroke_width=0.5)
        
        ctr_dot = Dot(point=FrontWheel.get_center(), radius=0.01, color=RED)

        self.play(Create(Car), Create(Wheels), Create(grass_set), Write(title), Create(title_SR), run_time=1)

        R_to_P_line = Line(start=FrontWheel.get_center(), end=P.get_center(), color=YELLOW, stroke_width=0.5).add_updater(lambda p: p.become(Line(start=FrontWheel.get_center(), end=P.get_center(), color=YELLOW, stroke_width=0.5)))

        theta = MathTex(r"\theta", color=BLUE).scale(0.125).next_to(FrontWheel.get_center(), UP*0.06+RIGHT*0.12)
        theta_SR = SurroundingRectangle(theta, color=YELLOW, buff=0.025, stroke_width=0.5)

        w = MathTex(r"\vec{\omega} = \frac{\Delta\theta}{\Delta t}", color=BLUE).scale(0.125).next_to(FrontWheel.get_center(), UP*1.2)
        w_SR = SurroundingRectangle(w, color=YELLOW, buff=0.025, stroke_width=0.5)

        v_p = MathTex(r"\vec{v}_P = \text{Tangential velocity at }P", color=BLUE).scale(0.125).next_to(FrontWheel.get_center(), DOWN*1.2)
        v_SR = SurroundingRectangle(v_p, color=YELLOW, buff=0.025, stroke_width=0.5).add_updater(lambda r: r.become(SurroundingRectangle(v_p, color=YELLOW, buff=0.025, stroke_width=0.5)))

        vw = MathTex(r"\vec{v}_P = \omega r", color=BLUE).scale(0.125).next_to(v_p.get_center(), DOWN*0.7)

        alpha = MathTex(r"\vec{\alpha} = \frac{\Delta\vec{\omega}}{\Delta t}", color=BLUE).scale(0.125).next_to(FrontWheel.get_center(), DOWN*1.2)
        alpha_SR = SurroundingRectangle(alpha, color=YELLOW, buff=0.025, stroke_width=0.5).add_updater(lambda r: r.become(SurroundingRectangle(alpha, color=YELLOW, buff=0.025, stroke_width=0.5)))

        final_tex = MathTex(r"\text{As }r \text{, the distance from the center becomes}\\\text{larger, the tangential velocity increases.}").set_color_by_gradient(BLUE, WHITE).scale(0.125).next_to(v_p.get_center(), DOWN*0.1)

        for i in range(14):
            base_anims = [
                ApplyMethod(Car.shift, UP * 0.075,
                            rate_func=lambda a: math.sin(3*(math.pi * a))),
                ApplyMethod(grass_set.shift, LEFT * 5, rate_func=linear)
            ]
            if i == 0:
                extra = [
                    Uncreate(title_SR),
                    FadeOut(title),
                    Create(mg_car),
                    Write(mg_label),
                    Create(Fn_car),
                    Create(Fn_label)
                ]
                self.play(AnimationGroup(*base_anims), AnimationGroup(*extra), run_time=3)
            elif i == 1:
                extra = [
                    self.camera.frame.animate.scale(0.15).move_to(FrontWheel_i),
                    SW.animate.set_value(0.5),
                    FadeIn(P),
                    FadeIn(P_label)
                ]
                self.play(AnimationGroup(*base_anims), AnimationGroup(*extra), run_time=2)
            elif i == 2:
                extra = [
                    Car.animate.set_opacity(0),
                    grass_set.animate.set_opacity(0),
                    mg_label.animate.set_opacity(0),
                    Create(R_to_P_line),
                    FadeOut(FrontWheel_i),
                    FadeIn(ctr_dot),
                    FadeIn(R_line),
                    Create(P_a),
                    FadeIn(P_a_label)
                ]
                self.play(AnimationGroup(*base_anims), AnimationGroup(*extra, run_time=1))
            elif i == 3:
                angle_updater = Angle(R_line, R_to_P_line, color=YELLOW, stroke_width=0.5)
                angle_updater.add_updater(
                    lambda d: d.become(Angle(R_line, R_to_P_line,
                                            color=YELLOW, stroke_width=0.5))
                )
                self.play(AnimationGroup(*base_anims), FadeIn(angle_updater, run_time=1))
            elif i == 4:
                extra = [Create(theta)]
                self.play(AnimationGroup(*base_anims), AnimationGroup(*extra, run_time=1))
            elif i == 5:
                self.play(AnimationGroup(*base_anims), Create(theta_SR, run_time=0.1))
            elif i == 6:
                self.play(AnimationGroup(*base_anims),
                        AnimationGroup(Create(w),
                                        ReplacementTransform(theta_SR, w_SR),
                                        run_time=1))
            elif i == 7:
                self.play(AnimationGroup(*base_anims),
                        AnimationGroup(Create(v_p),
                                        Create(Pa_SR),
                                        ReplacementTransform(Pa_SR, v_SR),
                                        run_time=1.5))
            elif i == 8:
                self.play(AnimationGroup(*base_anims),
                        AnimationGroup(FadeOut(w_SR),
                                        FadeOut(v_SR),
                                        GrowFromPoint(vw, v_p.get_center()),
                                        run_time=1.5))
            elif i == 9:
                self.play(AnimationGroup(*base_anims),
                          AnimationGroup(ReplacementTransform(v_p, alpha), ReplacementTransform(w_SR, alpha_SR)),
                          run_time=1.5)
            elif i == 10:
                self.play(AnimationGroup(FadeOut(*[m for m in self.mobjects if m != v_p])),
                          v_p.animate.move_to(FrontWheel.get_center()),
                          run_time=1.5)
                self.remove(*[m for m in self.mobjects if m != v_p])
            elif i == 11:
                final_tex.shift(UP*0.15)
                self.play(Write(final_tex), run_time=1.5)
                self.wait(2)
            elif i == 12:
                self.play(AnimationGroup(FadeOut(v_p), FadeOut(final_tex)))
            elif i == 13:
                self.wait(1)
            else:
                self.play(AnimationGroup(*base_anims), run_time=1)
                self.wait(1)

# manim -pqh video10.py video10