from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class CongruenceTick(VGroup):
    def __init__(self, A, B, length=0.18, **kwargs):
        super().__init__(**kwargs)

        A = np.array(A)
        B = np.array(B)

        v = B - A
        v_hat = v / np.linalg.norm(v)

        perp = np.array([-v_hat[1], v_hat[0], 0])
        M = (A + B) / 2

        tick = Line(
            M - perp * (length/2),
            M + perp * (length/2),
            stroke_width=4
        )
        self.add(tick)


class video23(MovingCameraScene):
    def construct(self):
        
        self.camera.frame.scale(1.1)

        def intersection_of_lines(p1, p2, q1, q2):
            p1 = np.array(p1)
            p2 = np.array(p2)
            q1 = np.array(q1)
            q2 = np.array(q2)

            r = p2[:2] - p1[:2]
            s = q2[:2] - q1[:2]
            A = np.column_stack((r, -s))
            b = q1[:2] - p1[:2]
            t, _ = np.linalg.solve(A, b)
            intersection_xy = p1[:2] + t * r
            return np.array([intersection_xy[0], intersection_xy[1], 0])

        empty = MathTex("")

        title = Tex("Hard SAT Questions").set_color_by_gradient(BLUE, WHITE).shift(UP*4)
        q1of2 = Tex("Question 1 of 2").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(title, DOWN)
        q2of2 = Tex("Question 2 of 2").set_color_by_gradient(BLUE, WHITE).scale(0.9).next_to(title, DOWN)

        ACD = Polygon([-3, 0, 0], [3, 0, 0], [0, 2, 0], color=BLUE)
        BDE = Polygon([3, 4, 0], [-3, 0, 0], [1.5, 0, 0], color=BLUE)

        D = Tex("D", color=BLUE).next_to(ACD.get_vertices()[0], DL)
        C = Tex("C", color=BLUE).next_to(ACD.get_vertices()[2], UL)
        A = Tex("A", color=BLUE).next_to(ACD.get_vertices()[1], DR)
        E = Tex("E", color=BLUE).next_to(BDE.get_vertices()[2], DOWN)
        B = Tex("B", color=BLUE).next_to(BDE.get_vertices()[0], UR)

        F_pt = intersection_of_lines(BDE.get_vertices()[2], BDE.get_vertices()[0], ACD.get_vertices()[1], ACD.get_vertices()[2])
        F_dot = Dot(F_pt, color=BLUE)

        labels = VGroup(A, B, C, D, E)
        setup = VGroup(labels, ACD, BDE, F_dot)

        setup.scale(0.9)
        setup.shift(DOWN)

        # Recompute key points after applying the global transform so all derived geometry lines up
        A_pt = ACD.get_vertices()[1]
        C_pt = ACD.get_vertices()[2]
        D_pt = ACD.get_vertices()[0]
        B_pt = BDE.get_vertices()[0]
        E_pt = BDE.get_vertices()[2]
        F_pt = intersection_of_lines(E_pt, B_pt, A_pt, C_pt)
        F_dot.move_to(F_pt)

        xAng = MathTex(r"x^\circ").scale(0.8).move_to(BDE.get_vertices()[2]).shift(UP*0.25+RIGHT*0.35)
        xQ = MathTex(r"\text{What is the value of }x^\circ\text{?}").shift(DOWN*3)

        AC_tick = CongruenceTick(ACD.get_vertices()[1], ACD.get_vertices()[2]).set_color(BLUE).scale(1.5)
        CD_tick = CongruenceTick(ACD.get_vertices()[2], ACD.get_vertices()[0]).set_color(BLUE).scale(1.5)

        angle_EBC = Angle(
            Line(B_pt, E_pt),
            Line(B_pt, C_pt),
            radius=0.5,
            other_angle=True,
            color=BLUE
        )

        angle_BDE = Angle(
            Line(D_pt, B_pt),
            Line(D_pt, E_pt),
            radius=0.5,
            other_angle=True,
            color=BLUE
        )

        angle_CAD = Angle(
            Line(A_pt, D_pt),
            Line(A_pt, C_pt),
            radius=0.5,
            other_angle=True,
            color=BLUE
        )

        label_EBC = MathTex("45^\circ").scale(0.7).set_color(BLUE)
        label_EBC.next_to(angle_EBC, DL, buff=0.1).shift(RIGHT*0.15)
        label_BDE = MathTex("38^\circ").scale(0.7).set_color(BLUE)
        label_BDE.next_to(angle_BDE, RIGHT*0.75, buff=0.1)
        label_CAD = MathTex("38^\circ").scale(0.7).set_color(BLUE)
        label_CAD.next_to(angle_CAD, DOWN, buff=0.1)

        angle_ACD = Angle(
            Line(C_pt, A_pt),
            Line(C_pt, D_pt),
            radius=0.5,
            other_angle=True,
            color=BLUE
        )

        angle_ACB = Angle(
            Line(C_pt, A_pt),
            Line(C_pt, B_pt),
            radius=0.4,
            color=BLUE
        )

        label_ACD = MathTex("104^\circ").scale(0.7).set_color(BLUE)
        label_ACD.next_to(angle_ACD, DOWN, buff=0.1)

        label_ACB = MathTex("76^\circ").scale(0.7).set_color(BLUE)
        label_ACB.next_to(angle_ACB, RIGHT*1.1, buff=0.1)

        angle_BFC = Angle(
            Line(F_pt, B_pt),
            Line(F_pt, C_pt),
            radius=0.3,
            color=YELLOW
        )

        angle_AFE = Angle(
            Line(F_pt, A_pt),
            Line(F_pt, E_pt),
            radius=0.3,
            color=YELLOW,
            other_angle=True
        )

        self.play(Create(ACD), Create(BDE), Create(AC_tick), Create(CD_tick),
                 Create(F_dot), Write(labels), Write(title), Create(angle_EBC), Write(label_EBC),
                Create(angle_ACD), Write(label_ACD), Write(q1of2),
                  run_time=1)

        self.play(Write(xAng), Write(xQ), run_time=1)
        self.play(Circumscribe(xQ))
        self.wait(1)

        since = MathTex(r"\text{since }\triangle ACD \text{ is isosceles}").scale(0.8).set_color_by_gradient(BLUE, WHITE).move_to(xQ.get_center())
        weknow = MathTex(r"\text{We know }\angle CAD=\angle BDE = \frac{1}{2}(180-104)").scale(0.8).set_color_by_gradient(BLUE, WHITE).next_to(since, UP)

        weknow2 = MathTex(r"\text{We know }\angle CAD=\angle BDE = \frac{1}{2}76").scale(0.8).set_color_by_gradient(BLUE, WHITE).move_to(weknow.get_center())
        weknow3 = MathTex(r"\text{We know }"+r"\angle CAD=\angle BDE = 38^\circ", substrings_to_isolate=[r"\angle CAD=\angle BDE = 38"]).scale(0.8).set_color_by_gradient(BLUE, WHITE).move_to(weknow.get_center())

        wk3SR = SurroundingRectangle(weknow3[1], color=YELLOW, buff=0.2)
        wk3SRC = wk3SR.copy()
        bde = SurroundingRectangle(label_BDE, color=YELLOW, buff=0.2)
        cad = SurroundingRectangle(label_CAD, color=YELLOW, buff=0.2)

        self.play(FadeOut(xQ), Write(weknow))
        self.play(Write(since))
        self.wait(0.25)
        self.play(TransformMatchingShapes(weknow, weknow2))
        self.wait(0.25)
        self.play(TransformMatchingShapes(weknow2, weknow3))
        self.wait(0.25)
        self.play(Create(wk3SR))
        self.play(ReplacementTransform(wk3SR, bde), ReplacementTransform(wk3SRC, cad),
                  FadeIn(angle_BDE, angle_CAD, label_BDE, label_CAD))
        self.play(FadeOut(bde, cad))
        self.wait(1)
        cSR = SurroundingRectangle(Dot(point=C_pt), color=YELLOW, buff=0.6)
        self.play(Create(cSR))

        supplementary = MathTex(r"\angle ACB = 180 - \angle ACD", color=YELLOW).scale(0.8).next_to(C_pt, UP*3.25+LEFT*0.75)
        supplementary1 = MathTex(r"\angle ACB = 180 - 104", color=YELLOW).scale(0.8).next_to(C_pt, UP*3.25+LEFT*0.75)
        supplementary2 = MathTex(r"\angle ACB = 76^\circ", color=YELLOW).scale(0.8).next_to(C_pt, UP*3.25+LEFT*0.75)

        angleFText = MathTex(r"180-(76+45)", color=YELLOW).scale(0.7).next_to(angle_BFC, UP*0.5)
        angleFText2 = MathTex(r"180-121", color=YELLOW).scale(0.7).next_to(angle_BFC, UP*0.5)
        angleFText3 = MathTex(r"59^\circ", color=YELLOW).scale(0.7).next_to(angle_BFC, UP*0.5)

        vertical_angles = MathTex(r"\text{Vertical Angles }\rightarrow", color=YELLOW).scale(0.7).move_to(ACD.get_center()+DOWN*0.5)

        self.wait(0.25)
        self.play(Write(supplementary))
        self.wait(0.25)
        self.play(TransformMatchingShapes(supplementary, supplementary1))
        self.wait(0.25)
        self.play(TransformMatchingShapes(supplementary1, supplementary2))
        self.play(FadeOut(cSR, supplementary2), Create(angle_ACB), Create(label_ACB))
        self.play(Create(angle_BFC), Write(angleFText))
        self.wait(0.25)
        self.play(TransformMatchingShapes(angleFText, angleFText2))
        self.wait(0.25)
        self.play(TransformMatchingShapes(angleFText2, angleFText3))
        self.wait(0.5)
        self.play(Write(vertical_angles))
        self.play(FadeIn(angle_AFE))

        finalans = MathTex(r"x=180-(59+38)", color=YELLOW).move_to(weknow3)
        finalans2 = MathTex(r"x=180-97", color=YELLOW).move_to(weknow3)
        finalans3 = MathTex(r"x=83^\circ").move_to(weknow3).set_color_by_gradient(BLUE, WHITE)

        self.wait(0.25)
        self.play(FadeOut(since), TransformMatchingShapes(weknow3, finalans))
        self.wait(0.25)
        self.play(TransformMatchingShapes(finalans, finalans2))
        self.wait(0.25)
        self.play(TransformMatchingShapes(finalans2, finalans3))
        self.play(Circumscribe(finalans3))
        self.wait(2)
        self.play(FadeOut(*[m for m in self.mobjects if m is not title and m is not q1of2]))

        W_point = np.array([-3.5, 1.6, 0])
        X_point = np.array([-3.8, -1.6, 0])
        Y_point = np.array([3.8, 1.6, 0])
        Z_point = np.array([3.5, -1.6, 0])
        Q_point = np.array([0, 0, 0])

        W_dot = Dot(W_point, radius=0.05, color=BLUE)
        X_dot = Dot(X_point, radius=0.05, color=BLUE)
        Y_dot = Dot(Y_point, radius=0.05, color=BLUE)
        Z_dot = Dot(Z_point, radius=0.05, color=BLUE)
        Q_dot = Dot(Q_point, radius=0.05, color=YELLOW)

        WQ_line = Line(W_point, Q_point, color=BLUE)
        QX_line = Line(Q_point, X_point, color=BLUE)
        WX_line = Line(W_point, X_point, color=BLUE)
        YQ_line = Line(Y_point, Q_point, color=BLUE)
        QZ_line = Line(Q_point, Z_point, color=BLUE)
        YZ_line = Line(Y_point, Z_point, color=BLUE)
        WZ_line = Line(W_point, Z_point, color=BLUE)
        XY_line = Line(X_point, Y_point, color=BLUE)

        W_label = Tex("W", color=BLUE).next_to(W_point, UL)
        X_label = Tex("X", color=BLUE).next_to(X_point, DL)
        Y_label = Tex("Y", color=BLUE).next_to(Y_point, UR)
        Z_label = Tex("Z", color=BLUE).next_to(Z_point, DR)
        Q_label = Tex("Q", color=BLUE).next_to(Q_point, DOWN, buff=0.2)

        intersect_setup = VGroup(
            WQ_line, QX_line, WX_line,
            YQ_line, QZ_line, YZ_line,
            WZ_line, XY_line,
            W_dot, X_dot, Y_dot, Z_dot, Q_dot,
            W_label, X_label, Y_label, Z_label, Q_label
        )
        intersect_setup.scale(0.9)
        intersect_setup.shift(DOWN * 0.5)

        self.play(Create(WQ_line), Create(QX_line), Create(WX_line),
                  Create(YQ_line), Create(QZ_line), Create(YZ_line),
                  Create(WZ_line), Create(XY_line),
                  FadeIn(W_dot, X_dot, Y_dot, Z_dot, Q_dot),
                  Write(VGroup(W_label, X_label, Y_label, Z_label, Q_label)), TransformMatchingShapes(q1of2, q2of2),
                  run_time=1.5)

        W_pt = W_dot.get_center()
        X_pt = X_dot.get_center()
        Y_pt = Y_dot.get_center()
        Z_pt = Z_dot.get_center()
        Q_pt = Q_dot.get_center()

        question2 = MathTex(r"\text{What is the length of } YZ\text{?}").scale(0.8).shift(DOWN * 3)
        current_label = question2
        self.play(Write(current_label))
        self.play(Circumscribe(current_label))
        self.wait(0.5)

        def length_label(text, start, end, shift):
            midpoint = (start + end) / 2
            return MathTex(text, color=BLUE).scale(0.9).move_to(midpoint + shift)

        YQ_length = length_label("63", Y_pt, Q_pt, UP*0.5)
        WQ_length = length_label("70", W_pt, Q_pt, UP*0.5)
        WX_length = length_label("60", W_pt, X_pt, LEFT*0.5)
        XQ_length = length_label("120", X_pt, Q_pt, DOWN * 0.45)
        question_mark = MathTex("?").set_color(YELLOW).move_to((Y_pt + Z_pt) / 2 + RIGHT * 0.25)

        length_labels = VGroup(YQ_length, WQ_length, WX_length, XQ_length, question_mark)
        self.play(FadeIn(length_labels, scale=1.2))
        self.play(LaggedStart(Indicate(YQ_line), Indicate(WQ_line), Indicate(WX_line), Indicate(QX_line), lag_ratio=0.15))

        angle_W = Angle(Line(W_pt, Q_pt), Line(W_pt, X_pt), radius=0.45, other_angle=True, color=YELLOW)
        angle_Y = Angle(Line(Y_pt, Q_pt), Line(Y_pt, Z_pt), radius=0.45, other_angle=False, color=YELLOW)
        angle_Q_left = Angle(Line(Q_pt, W_pt), Line(Q_pt, X_pt), radius=0.45, other_angle=False, color=YELLOW)
        angle_Q_right = Angle(Line(Q_pt, Y_pt), Line(Q_pt, Z_pt), radius=0.45, other_angle=True, color=YELLOW)

        a_label_W = MathTex("a^\circ", color=YELLOW).scale(0.8).next_to(angle_W, DOWN+RIGHT*0.225, buff=0.05)
        a_label_Y = MathTex("a^\circ", color=YELLOW).scale(0.8).next_to(angle_Y, DOWN+LEFT*0.225, buff=0.05)

        self.play(Create(angle_W), Create(angle_Y), FadeIn(a_label_W, a_label_Y))
        self.wait(0.25)
        self.play(Create(angle_Q_left), Create(angle_Q_right))
        self.wait(0.25)

        since_equal = MathTex(r"\text{since }\angle W = \angle Y = a^\circ").scale(0.75).set_color_by_gradient(BLUE, WHITE).move_to(question2.get_center())
        vertical_equal = MathTex(r"\text{and }\angle WQX = \angle YQZ").scale(0.75).set_color_by_gradient(BLUE, WHITE).move_to(question2.get_center())
        similarity_text = MathTex(r"\triangle WQX \sim \triangle YQZ").scale(0.85).set_color_by_gradient(BLUE, WHITE).move_to(question2.get_center())

        self.play(TransformMatchingShapes(current_label, since_equal))
        current_label = since_equal
        self.wait(0.5)
        self.play(TransformMatchingShapes(current_label, vertical_equal))
        current_label = vertical_equal
        self.wait(0.25)
        self.play(TransformMatchingShapes(current_label, similarity_text))
        current_label = similarity_text
        self.wait(0.5)

        left_highlight = Polygon(W_pt, Q_pt, X_pt, color=BLUE, fill_opacity=0.15, stroke_width=0)
        right_highlight = Polygon(Y_pt, Q_pt, Z_pt, color=BLUE, fill_opacity=0.15, stroke_width=0)
        self.play(FadeIn(left_highlight), FadeIn(right_highlight))

        scale_text = MathTex(r"\text{Scale factor }=\frac{YQ}{WQ}=\frac{63}{70}=0.9").scale(0.75).set_color_by_gradient(BLUE, WHITE).move_to(current_label.get_center())
        qz_text = MathTex(r"QZ = XQ \cdot \frac{YQ}{WQ} = 120 \cdot \frac{63}{70} = 108").scale(0.75).set_color_by_gradient(BLUE, WHITE).move_to(current_label.get_center())
        ratio_text = MathTex(r"\frac{WX}{YZ} = \frac{WQ}{YQ}").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(current_label.get_center())

        self.play(TransformMatchingShapes(current_label, scale_text))
        current_label = scale_text
        self.wait(0.5)
        self.play(TransformMatchingShapes(current_label, qz_text), Indicate(QX_line), Indicate(QZ_line))
        current_label = qz_text
        self.wait(0.25)
        self.play(TransformMatchingShapes(current_label, ratio_text), Indicate(WX_line), Indicate(YZ_line), Indicate(WQ_line), Indicate(YQ_line))
        current_label = ratio_text
        self.wait(0.25)

        substitution = MathTex(r"\frac{60}{YZ} = \frac{70}{63}").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(current_label.get_center())
        cross_mult = MathTex(r"60 \cdot 63 = 70 \cdot YZ").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(current_label.get_center())
        yz_value = MathTex(r"YZ = 54").scale(0.9).set_color_by_gradient(BLUE, WHITE).move_to(current_label.get_center())

        self.play(TransformMatchingShapes(current_label, substitution))
        current_label = substitution
        self.wait(0.25)
        self.play(TransformMatchingShapes(current_label, cross_mult))
        current_label = cross_mult
        self.wait(0.25)
        self.play(TransformMatchingShapes(current_label, yz_value))
        current_label = yz_value
        self.wait(0.25)

        final_label = MathTex("54").set_color(YELLOW).move_to(question_mark.get_center()+RIGHT*0.15)
        self.play(Transform(question_mark, final_label), YZ_line.animate.set_color(YELLOW))
        self.play(Circumscribe(yz_value))

        self.wait(2)
        self.play(FadeOut(*[m for m in self.mobjects]))

# manim -pqh video23.py video23