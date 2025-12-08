from manim import *
import math, numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video16(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        title = Tex("Law of Sines").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2).add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        self.play(Write(title), Create(titleSR))
        self.play(title.animate.shift(UP*4), Uncreate(titleSR))

        triangle = Polygon([-2, 0, 0], [2, 0, 0], [-0.5, 3, 0]).set_color_by_gradient([BLUE, WHITE])

        # Fix A to interior arc
        A = Angle(Line(start=[-2, 0, 0], end=[2, 0, 0]), Line(start=[-2, 0, 0], end=[-0.5, 3, 0]), color=BLUE, radius=0.5, other_angle=False)
        B = Angle(Line(start=[2, 0, 0], end=[-0.5, 3, 0]), Line(start=[2, 0, 0], end=[-2, 0, 0]), color=PURE_RED, radius=0.5)
        C = Angle(Line(start=[-0.5, 3, 0], end=[-2, 0, 0]), Line(start=[-0.5, 3, 0], end=[2, 0, 0]), color=PURE_GREEN, radius=0.5)

        side_a = Line(triangle.get_vertices()[1], triangle.get_vertices()[2])  # opposite A
        side_b = Line(triangle.get_vertices()[2], triangle.get_vertices()[0])  # opposite B
        side_c = Line(triangle.get_vertices()[0], triangle.get_vertices()[1])  # opposite C

        ALabel = MathTex(r"A", color=BLUE).scale(0.8)
        BLabel = MathTex(r"B", color=PURE_RED).scale(0.8)
        CLabel = MathTex(r"C", color=PURE_GREEN).scale(0.8)

        aLabel = MathTex(r"a", color=BLUE).move_to(side_a.get_center()).shift(UR*0.25)
        bLabel = MathTex(r"b", color=PURE_RED).next_to(side_b.get_center(), LEFT*0.55+UP*(1/3))
        cLabel = MathTex(r"c", color=PURE_GREEN).next_to(side_c, DOWN)

        # Position along bisector
        def position_label(angle, label, vertex, end1, end2, buff=0.8):
            vec1 = np.array(end1) - np.array(vertex)
            vec2 = np.array(end2) - np.array(vertex)
            norm1 = vec1 / np.linalg.norm(vec1)
            norm2 = vec2 / np.linalg.norm(vec2)
            bisector = norm1 + norm2
            bisector /= np.linalg.norm(bisector)
            label.move_to(np.array(vertex) + bisector * buff)
            
        law = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}"
        ).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)
        
        # Numerators
        numerator_a = law[0][0]   # a
        numerator_b = law[0][7]   # b
        numerator_c = law[0][14]  # c

        # Denominators (grouped glyphs after each fraction bar)
        denominator_A = VGroup(law[0][2], law[0][3], law[0][4], law[0][5])  # sin A
        denominator_B = VGroup(law[0][9], law[0][10], law[0][11], law[0][12])  # sin B
        denominator_C = VGroup(law[0][16], law[0][17], law[0][18], law[0][19])  # sin C

        # Make numerators invisible
        numerator_a.set_opacity(0)
        numerator_b.set_opacity(0)
        numerator_c.set_opacity(0)
        denominator_A.set_opacity(0).set_color(BLUE)
        denominator_B.set_opacity(0).set_color(PURE_RED)
        denominator_C.set_opacity(0).set_color(PURE_GREEN)

        position_label(A, ALabel, [-2, 0, 0], [2, 0, 0], [-0.5, 3, 0])
        position_label(B, BLabel, [2, 0, 0], [-0.5, 3, 0], [-2, 0, 0])
        position_label(C, CLabel, [-0.5, 3, 0], [-2, 0, 0], [2, 0, 0])

        self.play(Create(triangle), Create(A), Create(B), Create(C),
                  Create(ALabel), Create(BLabel), Create(CLabel),
                  Create(aLabel), Create(bLabel), Create(cLabel),
                  Create(law))

        aC = aLabel.copy()
        AC = ALabel.copy()

        self.play(aC.animate.move_to(numerator_a.get_center()), AC.animate.move_to(denominator_A.get_center()), denominator_A.animate.set_opacity(1), ReplacementTransform(AC, denominator_A))
        bC = bLabel.copy()
        BC = BLabel.copy()

        self.play(bC.animate.move_to(numerator_b.get_center()), BC.animate.move_to(denominator_B.get_center()), denominator_B.animate.set_opacity(1), ReplacementTransform(BC, denominator_B))
        cC = cLabel.copy()
        CC = CLabel.copy()

        self.play(cC.animate.move_to(numerator_c.get_center()), CC.animate.move_to(denominator_C.get_center()), denominator_C.animate.set_opacity(1), ReplacementTransform(CC, denominator_C))
        self.play(Circumscribe(law))

        exampleProblem = Tex("1: Example Problem").scale(0.8).next_to(bC, UP).set_color_by_gradient(BLUE, WHITE)

        rect = SurroundingRectangle(exampleProblem, color=[BLUE, WHITE], stroke_width=1.5, buff=0.1)
        
        elapsed = [0]
        duration = 28
        
        def grow(mob, dt):
            elapsed[0] = min(elapsed[0] + dt, duration)
            alpha = elapsed[0] / duration
            mob.pointwise_become_partial(
                SurroundingRectangle(exampleProblem, color=[BLUE, WHITE], stroke_width=1.5, buff=0.1),
                0, alpha
            )
        
        rect.add_updater(grow)

        self.play(Write(exampleProblem), run_time=1)
        self.add(rect)

        self.wait(0.25)

        a16 = MathTex(r"16", color=BLUE).scale(0.75).move_to(aLabel.get_center())
        aAng = MathTex(fr"{A.get_value() * 180 / PI:.0f}^\circ", color=BLUE).scale(0.65).move_to(ALabel.get_center())
        bAng = MathTex(fr"{B.get_value() * 180 / PI:.0f}^\circ", color=PURE_RED).scale(0.65).move_to(BLabel.get_center())
        cAng = MathTex(r"67^\circ", color=PURE_GREEN).scale(0.65).move_to(CLabel.get_center())

        findc = MathTex(r"\text{Find }c", color=PURE_GREEN).scale(0.75).next_to(exampleProblem, DOWN)
        findcSR = SurroundingRectangle(findc, color=YELLOW, buff=0.1)
        cSR = SurroundingRectangle(cLabel, color=YELLOW, buff=0.1)

        self.play(Transform(aLabel, a16), Transform(ALabel, aAng), Transform(BLabel, bAng),
                  FadeOut(CLabel), FadeOut(cLabel), FadeOut(bLabel), FadeOut(law), FadeOut(aC), FadeOut(AC), FadeOut(bC), FadeOut(BC), FadeOut(cC), FadeOut(CC))
        self.play(Write(findc))
        self.play(Create(findcSR))
        self.play(ReplacementTransform(findcSR, cSR), FadeIn(cLabel))
        self.play(Uncreate(cSR))

        self.play(ReplacementTransform(findc, law), Write(aC), Write(bC), Write(cC))
        self.wait(0.25)

        dA = denominator_A.copy()
        dC = denominator_C.copy()

        law2 = MathTex(
            r"\frac{\phantom{a}}{\phantom{\sin A}} = \frac{\phantom{c}}{\phantom{\sin C}}"
        ).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)
        self.play(TransformMatchingShapes(law, law2), FadeOut(bC), aC.animate.move_to(law2[0][0].get_center()+UP*0.25),
                  cC.animate.move_to(law2[0][2].get_center()+UP*0.25), dA.animate.move_to(law2[0][0].get_center()+DOWN*0.25),
                  dC.animate.move_to(law2[0][2].get_center()+DOWN*0.25))
        
        dCSR = SurroundingRectangle(dC, color=YELLOW, buff=0.1)
        CLabelSR = SurroundingRectangle(CLabel, color=YELLOW, buff=0.1)
        self.play(Create(dCSR))
        self.play(ReplacementTransform(dCSR, CLabelSR), FadeIn(CLabel))
        self.play(Uncreate(CLabelSR))

        anglesum = MathTex("A"+"+"+"B"+"+"+"C"+"=180", substrings_to_isolate=["A", "B", "C"]).scale(0.8).next_to(law2, DOWN*3).set_color_by_gradient(BLUE, WHITE)
        anglesum2 = MathTex("63"+"+"+"50"+"+"+"C"+"=180", substrings_to_isolate=["63", "50", "C"]).scale(0.8).next_to(law2, DOWN*3).set_color_by_gradient(BLUE, WHITE)
        anglesum3 = MathTex("113"+"+"+"C"+"=180", substrings_to_isolate=["113", "C"]).scale(0.8).next_to(law2, DOWN*3).set_color_by_gradient(BLUE, WHITE)
        anglesum4 = MathTex("C"+"=180"+"-113", substrings_to_isolate=["C", "-113"]).scale(0.8).next_to(law2, DOWN*3).set_color_by_gradient(BLUE, WHITE)
        anglesum5 = MathTex(r"C=67^\circ", color=PURE_GREEN).scale(0.8).next_to(law2, DOWN*3)

        anglesum[0].set_color(BLUE)
        anglesum[2].set_color(PURE_RED)
        anglesum[4].set_color(PURE_GREEN)

        anglesum2[0].set_color(BLUE)
        anglesum2[2].set_color(PURE_RED)
        anglesum2[4].set_color(PURE_GREEN)

        anglesum3[0].set_color_by_gradient(PURE_RED, BLUE)
        anglesum3[2].set_color(PURE_GREEN)

        anglesum4[0].set_color(PURE_GREEN)
        anglesum4[2].set_color_by_gradient(PURE_RED, BLUE)

        self.play(Write(anglesum))
        self.wait(0.25)
        self.play(TransformMatchingShapes(anglesum, anglesum2))
        self.wait(0.25)
        self.play(TransformMatchingShapes(anglesum2, anglesum3))
        self.wait(0.25)
        self.play(TransformMatchingShapes(anglesum3, anglesum4))
        self.wait(0.25)
        self.play(TransformMatchingShapes(anglesum4, anglesum5))

        anglesum5SR = SurroundingRectangle(anglesum5, color=YELLOW, buff=0.1)
        cAngSR = SurroundingRectangle(cAng, color=YELLOW, buff=0.1)

        law3 = MathTex(
            r"\phantom{67^\circ}"+r"\frac{\phantom{a}}{\phantom{\sin A}}"+r"=\phantom{c}",
            substrings_to_isolate=[r"\phantom{67^\circ}", r"\frac{\phantom{a}}{\phantom{\sin A}}"]
        ).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)

        self.play(Create(anglesum5SR))
        self.play(ReplacementTransform(anglesum5SR, cAngSR), TransformMatchingShapes(CLabel, cAng), FadeOut(anglesum5))
        self.play(Uncreate(cAngSR))
        self.wait(0.5)

        acop = a16.copy().move_to(aC.get_center())
        aangcop = MathTex(r"\sin(63^\circ)", color=BLUE).scale(0.65).move_to(dA.get_center())
        cangcop = MathTex(r"\sin(67^\circ)", color=PURE_GREEN).scale(0.65).move_to(dC.get_center())

        self.play(Circumscribe(aC), Transform(aC, acop))
        self.play(Circumscribe(dA), Transform(dA, aangcop))
        self.play(Circumscribe(dC), Transform(dC, cangcop))

        self.wait(0.25)

        self.remove(aC, dA, dC)
        self.play(TransformMatchingShapes(law2, law3),
                  cangcop.animate.move_to(law3[1].get_center()+LEFT*1.15),
                  acop.animate.move_to(law3[1].get_center()+UP*0.25),
                  aangcop.animate.move_to(law3[1].get_center()+DOWN*0.25),
                  cC.animate.move_to(law3[2].get_center()+RIGHT*0.375))
        
        els = VGroup(cangcop, acop, aangcop, cC, law3)
        ans = MathTex(r"c\approx 16.53", color=PURE_GREEN).scale(0.8).move_to(law3.get_center())

        self.wait(0.25)

        self.play(TransformMatchingShapes(els, ans))
        ansSR = SurroundingRectangle(ans, color=YELLOW, buff=0.1)
        self.play(Create(ansSR))

        cValue = MathTex(r"16.53", color=PURE_GREEN).scale(0.75).next_to(side_c, DOWN)
        
        cValueSR = SurroundingRectangle(cValue, color=YELLOW, buff=0.1)

        self.play(ReplacementTransform(ansSR, cValueSR), ReplacementTransform(cLabel, cValue))
        self.play(Uncreate(cValueSR))

        proof = Tex("2: Proof").scale(0.8).next_to(bC, UP).set_color_by_gradient(BLUE, WHITE)

        self.wait(0.5)

        target_ALabel = MathTex(r"A", color=BLUE).scale(0.8)
        position_label(A, target_ALabel, [-2, 0, 0], [2, 0, 0], [-0.5, 3, 0])
        target_BLabel = MathTex(r"B", color=PURE_RED).scale(0.8)
        position_label(B, target_BLabel, [2, 0, 0], [-0.5, 3, 0], [-2, 0, 0])
        target_CLabel = MathTex(r"C", color=PURE_GREEN).scale(0.8)
        position_label(C, target_CLabel, [-0.5, 3, 0], [-2, 0, 0], [2, 0, 0])
        target_aLabel = MathTex(r"a", color=BLUE).move_to(side_a.get_center()).shift(UR*0.25)
        target_cLabel = MathTex(r"c", color=PURE_GREEN).next_to(side_c, DOWN)

                
        elapsed = [0]
        duration = 29
        rect.add_updater(grow)
        self.add(rect)
        self.play(TransformMatchingShapes(exampleProblem, proof), TransformMatchingShapes(ALabel, target_ALabel), TransformMatchingShapes(BLabel, target_BLabel), FadeOut(CLabel),
                  TransformMatchingShapes(aLabel, target_aLabel), Write(bLabel), TransformMatchingShapes(cValue, target_cLabel), FadeOut(ans), FadeOut(cAng),
                  FadeOut(cLabel))

        hLine = Line(
            start=[-0.5, 3, 0],
            end=[-0.5, 0, 0],
            color=PINK,
            stroke_width=5
        )
        hLabel = MathTex(r"h", color=PINK).next_to(hLine, RIGHT)

        sinA = MathTex(r"\sin (A) = h / b", substrings_to_isolate=["h", "b"]
                       ).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)
        sinA[1].set_opacity(0)
        sinA[3].set_opacity(0)
        sinA2 = MathTex(r"b \, \sin (A) = h", substrings_to_isolate=["b", "h"]
                       ).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)
        sinA2[0].set_opacity(0)
        sinA2[2].set_opacity(0)

        hcop = hLabel.copy().scale(0.8)
        bcop2 = bLabel.copy().scale(0.8)

        sinB = MathTex(r"\sin (B) = h / a", substrings_to_isolate=["h", "a"]
                       ).scale(0.8).shift(DOWN*3).set_color_by_gradient(BLUE, WHITE)
        sinB[1].set_opacity(0)
        sinB[3].set_opacity(0)
        sinB2 = MathTex(r"a \, \sin (B) = h", substrings_to_isolate=["a", "h"]
                       ).scale(0.8).shift(DOWN*3).set_color_by_gradient(BLUE, WHITE)
        sinB2[0].set_opacity(0)
        sinB2[2].set_opacity(0)

        t1 = Polygon([-2, 0, 0], [-0.5, 3, 0], [-0.5, 0, 0], color=YELLOW)
        t2 = Polygon([2, 0, 0], [-0.5, 3, 0], [-0.5, 0, 0], color=YELLOW)

        hcop2 = hLabel.copy().scale(0.8)
        acop2 = MathTex(r"a", color=BLUE).scale(0.8)

        self.wait(0.25)
        self.play(FadeOut(C), Create(hLine), Write(hLabel))
        self.wait(0.25)
        self.play(Write(sinA), Create(t1))
        self.play(hcop.animate.move_to(sinA[1].get_center()), bcop2.animate.move_to(sinA[3].get_center()))
        self.wait(0.25)
        self.play(TransformMatchingTex(sinA, sinA2), hcop.animate.move_to(sinA2[2].get_center()),
                  bcop2.animate.move_to(sinA2[0].get_center()))
        self.wait(0.25)
        self.play(Write(sinB), ReplacementTransform(t1, t2))
        self.play(hcop2.animate.move_to(sinB[1].get_center()), acop2.animate.move_to(sinB[3].get_center()))
        self.wait(0.25)
        self.play(TransformMatchingTex(sinB, sinB2), hcop2.animate.move_to(sinB2[2].get_center()),
                  acop2.animate.move_to(sinB2[0].get_center()))
        
        neweq = MathTex(r"b \sin (A) = a \sin (B)", substrings_to_isolate=["a", "h"]
                       ).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)
        
        neweq2 = MathTex(r"\frac{a}{\sin (A)}"+"="+r"\frac{b}{\sin (B)}",
                       substrings_to_isolate=[r"\frac{a}{\sin (A)}", r"\frac{b}{\sin (B)}"]).scale(0.8).shift(DOWN*2).set_color_by_gradient(BLUE, WHITE)

        neweq2[1].set_color(BLUE)
        neweq2[2].set_color(PURE_RED)
        self.wait(0.5)
        self.play(TransformMatchingShapes(sinA2, neweq), TransformMatchingShapes(sinB2, neweq),
                  FadeOut(hcop, hcop2, bcop2, acop2, t2))
        self.wait(0.5)
        self.remove(neweq)
        self.play(TransformMatchingShapes(neweq, neweq2))
        self.wait(1)
        cC.move_to(numerator_c.get_center())
        aC = MathTex(r"a", color=BLUE).move_to(numerator_a.get_center())

        self.play(TransformMatchingShapes(neweq2, law), Write(aC), Write(AC), Write(bC), Write(BC), Write(cC), Write(CC))

        explanation = Tex("Always works for ASA and AAS").scale(0.8).next_to(law, DOWN).set_color_by_gradient(BLUE, WHITE)
        self.play(Write(explanation))
        self.play(Circumscribe(explanation))

        self.wait(1)

        fl = [aC, bC, cC, AC, BC, CC, law]

        finalLaw = VGroup(aC, bC, cC, AC, BC, CC, law)

        self.play(FadeOut(*[m for m in self.mobjects if m not in fl]), finalLaw.animate.move_to(ORIGIN))
        self.wait(0.25)
        
        finalLawSR = SurroundingRectangle(finalLaw, color=YELLOW, buff=0.2)

        self.play(Create(finalLawSR))
        self.play(FadeOut(finalLawSR))

        self.wait(2)
        self.play(FadeOut(finalLaw))

# manim -pqh video16.py video16