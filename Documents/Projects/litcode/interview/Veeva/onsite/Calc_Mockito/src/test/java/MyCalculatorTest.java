import static org.junit.Assert.*;
import static org.mockito.Mockito.*;

import org.junit.Before;
import org.junit.Test;


public class MyCalculatorTest {

    Calculator c = null;
    CalculatorService service = mock(CalculatorService.class);

    @Before
    public void setup() {
        c = new Calculator(service);
    }

    @Test
    public void testPerform() {
        when(service.add(2,3)).thenReturn(5);
        assertEquals(10, service.add(2,3));
        verify(service).add(2,3);
    }

}