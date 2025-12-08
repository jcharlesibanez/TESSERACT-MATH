from manim import *
import numpy as np

config.pixel_width= 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class video22(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.1)

        empty = MathTex("")

        title = Tex("How to Multiply Matrices").set_color_by_gradient(BLUE, WHITE)
        titleSR = SurroundingRectangle(title, color=YELLOW, buff=0.2)
        self.play(Write(title), Create(titleSR), run_time=1)
        
        titleSR.add_updater(lambda sr: sr.become(SurroundingRectangle(title, color=YELLOW, buff=0.2)))
        
        self.play(title.animate.shift(UP*4), Uncreate(titleSR), run_time=1)

        collection = MathTex("2", "3", "1", "5").set_color_by_gradient(BLUE, WHITE).arrange(RIGHT, buff=0.3).shift(UP*3)
        collection2 = MathTex("8", "2", "3", "9").set_color_by_gradient(BLUE, WHITE).arrange(RIGHT, buff=0.3).shift(UP*2)

        # Create the matrix with actual numbers
        m0 = Matrix([[2, 3], [1, 5]]).set_color(BLUE).shift(LEFT*1.5)
        # Make ONLY the elements invisible, keep brackets visible
        m0.get_entries().set_opacity(0)
        
        m1 = Matrix([[2, 3], [1, 5]]).set_color(BLUE).shift(LEFT*1.5)
        m2i = Matrix([[8, 2], [3, 9]]).set_color(BLUE).shift(RIGHT*1.5)
        m2i.get_entries().set_opacity(0)
        m2 = Matrix([[8, 2], [3, 9]]).set_color(BLUE).shift(RIGHT*1.5)

        m1_c = m1.copy()
        self.play(FadeIn(collection, m0, collection2, m2i))
        self.play(TransformMatchingShapes(collection, m1), Transform(m0, m1_c),
                  TransformMatchingShapes(collection2, m2), Transform(m2i, m2))
        self.remove(m1_c)
        self.remove(m0)
        self.remove(m2i)

        downbrace = BraceBetweenPoints(
            point_1=m1.get_corner(DL)+DOWN*0.25,
            point_2=m1.get_corner(DR)+DOWN*0.25,
            direction=DOWN
        ).set_color_by_gradient([BLUE, WHITE])

        upbrace = BraceBetweenPoints(
            point_1=m1.get_corner(DL)+LEFT*0.25,
            point_2=m1.get_corner(UL)+LEFT*0.25,
            direction=LEFT
        ).set_color_by_gradient([BLUE, WHITE])

        downbraceLabel = MathTex("2", color=BLUE).next_to(downbrace, DOWN*2).set_color_by_gradient(BLUE, WHITE).scale(0.8)
        upbraceLabel = MathTex("2", color=BLUE).next_to(upbrace, LEFT).set_color_by_gradient(BLUE, WHITE).scale(0.8)

        downbrace2 = BraceBetweenPoints(
            point_1=m2.get_corner(DL)+DOWN*0.25,
            point_2=m2.get_corner(DR)+DOWN*0.25,
            direction=DOWN
        ).set_color_by_gradient([BLUE, WHITE])

        upbrace2 = BraceBetweenPoints(
            point_1=m2.get_corner(DR)+RIGHT*0.25,
            point_2=m2.get_corner(UR)+RIGHT*0.25,
            direction=RIGHT
        ).set_color_by_gradient([BLUE, WHITE])

        downbraceLabel2 = MathTex("2", color=BLUE).next_to(downbrace2, DOWN*2).set_color_by_gradient(BLUE, WHITE).scale(0.8)
        upbraceLabel2 = MathTex("2", color=BLUE).next_to(upbrace2, RIGHT).set_color_by_gradient(BLUE, WHITE).scale(0.8)

        self.play(FadeIn(downbrace, upbrace, downbraceLabel, upbraceLabel,
                         downbrace2, upbrace2, downbraceLabel2, upbraceLabel2))

        twobytwo = MathTex(r"2"+ r"\times" +"2", substrings_to_isolate=["2", "2"]).set_color_by_gradient(BLUE, WHITE).next_to(m1, UP)
        m1CNL = SurroundingRectangle(twobytwo[2], color=YELLOW, buff=0.2)
        twobytwo2 = MathTex(r"2"+ r"\times" +"2", substrings_to_isolate=["2", "2"]).set_color_by_gradient(BLUE, WHITE).next_to(m2, UP)
        m2RNL = SurroundingRectangle(twobytwo2[0], color=YELLOW, buff=0.2)

        self.play(TransformMatchingShapes(downbraceLabel, twobytwo), TransformMatchingShapes(upbraceLabel, twobytwo),
                  FadeOut(downbrace, upbrace),
                  TransformMatchingShapes(downbraceLabel2, twobytwo2), TransformMatchingShapes(upbraceLabel2, twobytwo2),
                  FadeOut(downbrace2, upbrace2))
        
        self.play(Create(m1CNL), Create(m2RNL))
        multipliable0 = Tex("Number of columns in Matrix 1").set_color_by_gradient(BLUE, WHITE).shift(DOWN*1.5).scale(0.8)
        multipliable1 = Tex("=").set_color_by_gradient(BLUE, WHITE).next_to(multipliable0, DOWN*0.5).scale(0.8)
        multipliable2 = Tex("Number of rows in Matrix 2").set_color_by_gradient(BLUE, WHITE).next_to(multipliable1, DOWN*0.5).scale(0.8)
        
        self.play(FadeIn(multipliable0, multipliable1, multipliable2), Uncreate(m1CNL), Uncreate(m2RNL))

        mustbetrueBrace = Brace(
            mobject=multipliable2,
            direction=DOWN
        ).set_color_by_gradient([BLUE, WHITE])
        mustbetrueLabel = Tex("Must be true or you can't multiply").set_color_by_gradient(BLUE, WHITE).scale(0.8).next_to(mustbetrueBrace, DOWN)

        self.play(FadeIn(mustbetrueBrace, mustbetrueLabel))

        self.wait(0.5)

        self.play(FadeOut(mustbetrueLabel), FadeOut(mustbetrueBrace), FadeOut(multipliable0, multipliable1, multipliable2, twobytwo, twobytwo2))

        m3_ = Matrix([[25, 31], [23, 47]]).set_color(BLUE).shift(DOWN*2.5)
        m3_.get_entries().set_opacity(0)
        equalsm3 = MathTex("=", color=BLUE).next_to(m3_, LEFT)
        m3 = VGroup(equalsm3, m3_)
        times = MathTex(r"\times", color=BLUE).scale(1.25)

        self.play(TransformMatchingShapes(empty, times))
        self.play(FadeIn(m3))

        row1 = SurroundingRectangle(Line(start=m1.get_entries()[0].get_center(), end=m1.get_entries()[1].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        column1 = SurroundingRectangle(Line(start=m2.get_entries()[0].get_center(), end=m2.get_entries()[2].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        row2 = SurroundingRectangle(Line(start=m1.get_entries()[0].get_center(), end=m1.get_entries()[1].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        column2 = SurroundingRectangle(Line(start=m2.get_entries()[1].get_center(), end=m2.get_entries()[3].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        row3 = SurroundingRectangle(Line(start=m1.get_entries()[2].get_center(), end=m1.get_entries()[3].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        column3 = SurroundingRectangle(Line(start=m2.get_entries()[0].get_center(), end=m2.get_entries()[2].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        row4 = SurroundingRectangle(Line(start=m1.get_entries()[2].get_center(), end=m1.get_entries()[3].get_center()), color=YELLOW, buff=0.3, stroke_width=6)
        column4 = SurroundingRectangle(Line(start=m2.get_entries()[1].get_center(), end=m2.get_entries()[3].get_center()), color=YELLOW, buff=0.3, stroke_width=6)

        row1multiplication = MathTex("2", "3").set_color_by_gradient(BLUE, WHITE)
        row1multiplication.arrange(RIGHT, buff=1.5)
        column1multiplication = MathTex("8", "3").set_color_by_gradient(BLUE, WHITE)
        column1multiplication.arrange(RIGHT, buff=1.5)

        # Arrange them vertically with space for the times symbols and plus
        VGroup(row1multiplication, column1multiplication).arrange(DOWN, buff=0.75).next_to(times, UP*4)

        # Place multiplication signs between the numbers
        twotimeseight = MathTex(r"\times", color=BLUE).move_to([
            (row1multiplication[0].get_center()[0] + column1multiplication[0].get_center()[0])/2,
            (row1multiplication[0].get_center()[1] + column1multiplication[0].get_center()[1])/2,
            0
        ])

        threetimesthree = MathTex(r"\times", color=BLUE).move_to([
            (row1multiplication[1].get_center()[0] + column1multiplication[1].get_center()[0])/2,
            (row1multiplication[1].get_center()[1] + column1multiplication[1].get_center()[1])/2,
            0
        ])

        # Place plus between row1multiplication and column1multiplication
        plus = MathTex(r"+", color=BLUE).move_to([
            0,
            (row1multiplication.get_center()[1] + column1multiplication.get_center()[1])/2,
            0
        ])

        sixteen = MathTex("16", color=BLUE).move_to(twotimeseight.get_center())
        nine = MathTex("9", color=BLUE).move_to(threetimesthree.get_center())
        twentyfive = MathTex("25", color=BLUE).move_to(plus.get_center())

        self.play(Create(row1), Create(column1))
        self.play(TransformMatchingShapes(VGroup(m1.get_entries()[0].copy(), m1.get_entries()[1].copy()), row1multiplication),
                  TransformMatchingShapes(VGroup(m2.get_entries()[0].copy(), m2.get_entries()[2].copy()), column1multiplication))
        self.play(Create(twotimeseight), Create(threetimesthree), Create(plus))
        self.play(FadeOut(twotimeseight), TransformMatchingShapes(row1multiplication[0], sixteen), TransformMatchingShapes(column1multiplication[0], sixteen),
                  FadeOut(threetimesthree), TransformMatchingShapes(row1multiplication[1], nine), TransformMatchingShapes(column1multiplication[1], nine))
        self.play(FadeOut(plus), TransformMatchingShapes(sixteen, twentyfive), TransformMatchingShapes(nine, twentyfive))
        self.play(twentyfive.animate.move_to(m3_.get_entries()[0]))
        self.play(ReplacementTransform(row1, row2), ReplacementTransform(column1, column2))

        # SECOND STAGE - Row 1, Column 2
        row2multiplication = MathTex("2", "3").set_color_by_gradient(BLUE, WHITE)
        row2multiplication.arrange(RIGHT, buff=1.5)
        column2multiplication = MathTex("2", "9").set_color_by_gradient(BLUE, WHITE)
        column2multiplication.arrange(RIGHT, buff=1.5)

        VGroup(row2multiplication, column2multiplication).arrange(DOWN, buff=0.75).next_to(times, UP*4)

        twotimestwo = MathTex(r"\times", color=BLUE).move_to([
            (row2multiplication[0].get_center()[0] + column2multiplication[0].get_center()[0])/2,
            (row2multiplication[0].get_center()[1] + column2multiplication[0].get_center()[1])/2,
            0
        ])

        threetimesnine = MathTex(r"\times", color=BLUE).move_to([
            (row2multiplication[1].get_center()[0] + column2multiplication[1].get_center()[0])/2,
            (row2multiplication[1].get_center()[1] + column2multiplication[1].get_center()[1])/2,
            0
        ])

        plus2 = MathTex(r"+", color=BLUE).move_to([
            0,
            (row2multiplication.get_center()[1] + column2multiplication.get_center()[1])/2,
            0
        ])

        four = MathTex("4", color=BLUE).move_to(twotimestwo.get_center())
        twentyseven = MathTex("27", color=BLUE).move_to(threetimesnine.get_center())
        thirtyone = MathTex("31", color=BLUE).move_to(plus2.get_center())

        self.play(TransformMatchingShapes(VGroup(m1.get_entries()[0].copy(), m1.get_entries()[1].copy()), row2multiplication),
                  TransformMatchingShapes(VGroup(m2.get_entries()[1].copy(), m2.get_entries()[3].copy()), column2multiplication))
        self.play(Create(twotimestwo), Create(threetimesnine), Create(plus2))
        self.play(FadeOut(twotimestwo), TransformMatchingShapes(row2multiplication[0], four), TransformMatchingShapes(column2multiplication[0], four),
                  FadeOut(threetimesnine), TransformMatchingShapes(row2multiplication[1], twentyseven), TransformMatchingShapes(column2multiplication[1], twentyseven))
        self.play(FadeOut(plus2), TransformMatchingShapes(four, thirtyone), TransformMatchingShapes(twentyseven, thirtyone))
        self.play(thirtyone.animate.move_to(m3_.get_entries()[1]))
        self.play(ReplacementTransform(row2, row3), ReplacementTransform(column2, column3))

        # THIRD STAGE - Row 2, Column 1
        row3multiplication = MathTex("1", "5").set_color_by_gradient(BLUE, WHITE)
        row3multiplication.arrange(RIGHT, buff=1.5)
        column3multiplication = MathTex("8", "3").set_color_by_gradient(BLUE, WHITE)
        column3multiplication.arrange(RIGHT, buff=1.5)

        VGroup(row3multiplication, column3multiplication).arrange(DOWN, buff=0.75).next_to(times, UP*4)

        onetimeseight = MathTex(r"\times", color=BLUE).move_to([
            (row3multiplication[0].get_center()[0] + column3multiplication[0].get_center()[0])/2,
            (row3multiplication[0].get_center()[1] + column3multiplication[0].get_center()[1])/2,
            0
        ])

        fivetimesthree = MathTex(r"\times", color=BLUE).move_to([
            (row3multiplication[1].get_center()[0] + column3multiplication[1].get_center()[0])/2,
            (row3multiplication[1].get_center()[1] + column3multiplication[1].get_center()[1])/2,
            0
        ])

        plus3 = MathTex(r"+", color=BLUE).move_to([
            0,
            (row3multiplication.get_center()[1] + column3multiplication.get_center()[1])/2,
            0
        ])

        eight = MathTex("8", color=BLUE).move_to(onetimeseight.get_center())
        fifteen = MathTex("15", color=BLUE).move_to(fivetimesthree.get_center())
        twentythree = MathTex("23", color=BLUE).move_to(plus3.get_center())

        self.play(TransformMatchingShapes(VGroup(m1.get_entries()[2].copy(), m1.get_entries()[3].copy()), row3multiplication),
                  TransformMatchingShapes(VGroup(m2.get_entries()[0].copy(), m2.get_entries()[2].copy()), column3multiplication))
        self.play(Create(onetimeseight), Create(fivetimesthree), Create(plus3))
        self.play(FadeOut(onetimeseight), TransformMatchingShapes(row3multiplication[0], eight), TransformMatchingShapes(column3multiplication[0], eight),
                  FadeOut(fivetimesthree), TransformMatchingShapes(row3multiplication[1], fifteen), TransformMatchingShapes(column3multiplication[1], fifteen))
        self.play(FadeOut(plus3), TransformMatchingShapes(eight, twentythree), TransformMatchingShapes(fifteen, twentythree))
        self.play(twentythree.animate.move_to(m3_.get_entries()[2]))
        self.play(ReplacementTransform(row3, row4), ReplacementTransform(column3, column4))

        row4multiplication = MathTex("1", "5").set_color_by_gradient(BLUE, WHITE)
        row4multiplication.arrange(RIGHT, buff=1.5)
        column4multiplication = MathTex("2", "9").set_color_by_gradient(BLUE, WHITE)
        column4multiplication.arrange(RIGHT, buff=1.5)

        VGroup(row4multiplication, column4multiplication).arrange(DOWN, buff=0.75).next_to(times, UP*4)

        onetimestwo = MathTex(r"\times", color=BLUE).move_to([
            (row4multiplication[0].get_center()[0] + column4multiplication[0].get_center()[0])/2,
            (row4multiplication[0].get_center()[1] + column4multiplication[0].get_center()[1])/2,
            0
        ])

        fivetimesnine = MathTex(r"\times", color=BLUE).move_to([
            (row4multiplication[1].get_center()[0] + column4multiplication[1].get_center()[0])/2,
            (row4multiplication[1].get_center()[1] + column4multiplication[1].get_center()[1])/2,
            0
        ])

        plus4 = MathTex(r"+", color=BLUE).move_to([
            0,
            (row4multiplication.get_center()[1] + column4multiplication.get_center()[1])/2,
            0
        ])

        two = MathTex("2", color=BLUE).move_to(onetimestwo.get_center())
        fortyfive = MathTex("45", color=BLUE).move_to(fivetimesnine.get_center())
        fortyseven = MathTex("47", color=BLUE).move_to(plus4.get_center())

        self.play(TransformMatchingShapes(VGroup(m1.get_entries()[2].copy(), m1.get_entries()[3].copy()), row4multiplication),
                  TransformMatchingShapes(VGroup(m2.get_entries()[1].copy(), m2.get_entries()[3].copy()), column4multiplication))
        self.play(Create(onetimestwo), Create(fivetimesnine), Create(plus4))
        self.play(FadeOut(onetimestwo), TransformMatchingShapes(row4multiplication[0], two), TransformMatchingShapes(column4multiplication[0], two),
                  FadeOut(fivetimesnine), TransformMatchingShapes(row4multiplication[1], fortyfive), TransformMatchingShapes(column4multiplication[1], fortyfive))
        self.play(FadeOut(plus4), TransformMatchingShapes(two, fortyseven), TransformMatchingShapes(fortyfive, fortyseven))
        self.play(fortyseven.animate.move_to(m3_.get_entries()[3]))
        self.play(FadeOut(row4, column4))
        self.wait(0.25)

        A = MathTex("A", color=BLUE).next_to(m1, UP)
        B = MathTex("B", color=BLUE).next_to(m2, UP)
        C = MathTex("C", color=BLUE).next_to(m3_, UP)

        formula = MathTex("C=AB").set_color_by_gradient(BLUE, WHITE).shift(UP*1.75)

        self.play(FadeIn(A, B, C, formula))
        ij1 = MathTex(r"i\text{ rows, }j \text{ columns}").scale(0.65).next_to(m1, DOWN).set_color_by_gradient(BLUE, WHITE)
        ij2 = MathTex(r"i\text{ rows, }j \text{ columns}").scale(0.65).next_to(m2, DOWN).set_color_by_gradient(BLUE, WHITE)
        ij3 = MathTex(r"i\text{ rows, }j \text{ columns}").scale(0.65).next_to(m3_, DOWN).set_color_by_gradient(BLUE, WHITE)
        self.play(FadeIn(ij1, ij2, ij3))
        self.wait(1)

        cij = MathTex(r"c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}").move_to(formula.get_center()+UP*0.5).set_color_by_gradient(BLUE, WHITE)
        c11 = MathTex(r"c_{1,1}").scale(0.7).next_to(m3_.get_entries()[0], UP).set_color_by_gradient(BLUE, WHITE)
        c12 = MathTex(r"c_{1,2}").scale(0.7).next_to(m3_.get_entries()[1], UP).set_color_by_gradient(BLUE, WHITE)
        c21 = MathTex(r"c_{2,1}").scale(0.7).next_to(m3_.get_entries()[2], DOWN).set_color_by_gradient(BLUE, WHITE)
        c22 = MathTex(r"c_{2,2}").scale(0.7).next_to(m3_.get_entries()[3], DOWN).set_color_by_gradient(BLUE, WHITE)

        sr1 = SurroundingRectangle(m3_.get_entries()[0], color=BLUE, buff=0.1).set_opacity(0.5)
        sr2 = SurroundingRectangle(m3_.get_entries()[1], color=BLUE, buff=0.1).set_opacity(0.5)
        sr4 = SurroundingRectangle(m3_.get_entries()[2], color=BLUE, buff=0.1).set_opacity(0.5)
        sr3 = SurroundingRectangle(m3_.get_entries()[3], color=BLUE, buff=0.1).set_opacity(0.5)

        self.play(Write(cij), FadeIn(c11, c12, c21, c22), FadeOut(formula),
                  FadeIn(sr1, sr2, sr3, sr4))

        self.wait(1)
        self.play(FadeOut(sr1, sr2, sr3, sr4, c11, c12, c21, c22, C, m3, cij, ij1, ij2, ij3),
                        FadeOut(twentyfive, thirtyone, twentythree, fortyseven))

        noncommutative = Tex("Matrix multiplication is noncommutative").set_color_by_gradient(BLUE, WHITE).scale(0.9).move_to(cij.get_center())
        isassociative = Tex("Matrix multiplication is associative").set_color_by_gradient(BLUE, WHITE).scale(0.9).move_to(noncommutative.get_center())
        
        self.wait(0.25)
        self.play(FadeIn(noncommutative))
        
        comneq = MathTex(r"A\times B \neq B\times A").set_color_by_gradient(BLUE, WHITE).shift(DOWN*2)
        
        # Scale and shift the original matrices first
        self.play(
            VGroup(A, m1, times, B, m2).animate.scale(0.75).shift(LEFT*2.5)
        )
        
        # Create copies positioned correctly
        times2 = MathTex(r"\times", color=BLUE)
        neq = MathTex(r"\neq", color=BLUE).scale(0.75)
        
        # Position B×A on the right side
        Bcop = m2.copy()
        times2_pos = m2.get_right() + RIGHT*2.75
        Acop = m1.copy()
        
        times2.move_to(times2_pos)
        neq.next_to(m2, RIGHT)
        Bcop.next_to(times2, LEFT)
        Acop.next_to(times2, RIGHT)

        bcopl = MathTex("B", color=BLUE).next_to(Bcop, UP)
        acopl = MathTex("A", color=BLUE).next_to(Acop, UP)
        
        self.play(
            FadeIn(comneq),
            FadeIn(neq),
            TransformFromCopy(m2, Bcop),
            FadeIn(times2),
            TransformFromCopy(m1, Acop),
            TransformFromCopy(B, bcopl),
            TransformFromCopy(A, acopl)
        )

        self.wait(1)

        m2_brackets = m2.get_brackets()
        self.play(FadeOut(m1, times, m2, m2.copy(), neq, m2, Acop, Bcop, times2, A, B, acopl, bcopl, comneq))
        associative = MathTex("(AB)C=A(BC)").set_color_by_gradient(BLUE, WHITE)
        self.play(TransformMatchingShapes(noncommutative, isassociative))
        self.play(FadeIn(associative))

        m3g = VGroup(m3, twentyfive, thirtyone, twentythree, fortyseven)
        self.wait(1)

        VGroup(A, m1, times, B, m2).scale(1.25).shift(RIGHT*2.5)
        
        exceptions = [title, m1, times, m2, m2_brackets, m3, twentyfive, thirtyone, twentythree, fortyseven]
        for entry in m2.get_entries():
            exceptions.append(entry)
        for entry in m1.get_entries():
            exceptions.append(entry)

        self.play(FadeOut(associative, title, isassociative), FadeIn(m1, m2, m3, twentyfive, thirtyone, twentythree, fortyseven), run_time=1)

        self.play(
            FadeOut(*[m for m in self.mobjects if m not in exceptions and m is not m2]),
            m1.animate.shift(LEFT*1.75),
            times.animate.shift(LEFT*1.75),
            m2.animate.shift(LEFT*1.75),
            m3g.animate.move_to(m2.get_center()+RIGHT*1.25),
        )

        self.wait(1)

        self.play(FadeIn(cij))

        self.play(m1.get_entries()[0].animate.become(MathTex(r"a_{11}", color=BLUE).move_to(m1.get_entries()[0].get_center())),
                  m1.get_entries()[1].animate.become(MathTex(r"a_{12}", color=BLUE).move_to(m1.get_entries()[1].get_center())),
                  m1.get_entries()[2].animate.become(MathTex(r"a_{21}", color=BLUE).move_to(m1.get_entries()[2].get_center())),
                  m1.get_entries()[3].animate.become(MathTex(r"a_{22}", color=BLUE).move_to(m1.get_entries()[3].get_center())),
                  m2.get_entries()[0].animate.become(MathTex(r"b_{11}", color=BLUE).move_to(m2.get_entries()[0].get_center())),
                  m2.get_entries()[1].animate.become(MathTex(r"b_{12}", color=BLUE).move_to(m2.get_entries()[1].get_center())),
                  m2.get_entries()[2].animate.become(MathTex(r"b_{21}", color=BLUE).move_to(m2.get_entries()[2].get_center())),
                  m2.get_entries()[3].animate.become(MathTex(r"b_{22}", color=BLUE).move_to(m2.get_entries()[3].get_center())),
                  twentyfive.animate.become(MathTex(r"c_{11}", color=BLUE).move_to(m3_.get_entries()[0].get_center())),
                  thirtyone.animate.become(MathTex(r"c_{12}", color=BLUE).move_to(m3_.get_entries()[1].get_center())),
                  twentythree.animate.become(MathTex(r"c_{21}", color=BLUE).move_to(m3_.get_entries()[2].get_center())),
                  fortyseven.animate.become(MathTex(r"c_{22}", color=BLUE).move_to(m3_.get_entries()[3].get_center())))
        
        self.wait(2)

        self.play(FadeOut(*[m for m in self.mobjects]))

# manim -pqh video22.py video22