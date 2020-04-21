import static org.junit.Assert.assertEquals;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.verify;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CalculatorTest {

    Calculator c = null;
    CalculatorService service = mock(CalculatorService.class);

    @Before
    public void setUp(){
        c = new Calculator(service);
    }

    @Test
    public void testPerform() {
        when(service.add(2,3)).thenReturn(5);
        assertEquals(10, c.perform(2,3));
        verify(service).add(2,3);
    }
}