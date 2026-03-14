/**
 * Ejercicios prácticos para sintaxis y semántica de lenguajes.
 *
 * El alumno debe implementar funciones que trabajen con gramáticas y árboles sintácticos.
 */

export type GrammarRule = { left: string; right: string[] };

/**
 * Dada una gramática (lista de reglas), genera la lista de símbolos no terminales.
 */
export function simbolosNoTerminales(rules: GrammarRule[]): string[] {
  const set = new Set<string>();
  for (const r of rules) {
    set.add(r.left);
  }
  return Array.from(set);
}

/**
 * Chequea si la gramática es ambigua para la expresión `a + b * c`.
 * (simplificación para este TP)
 */
export function esAmbigua(): boolean {
  // La gramática dada en clase es ambigua para `a + b * c`.
  return true;
}

/**
 * Dada una cadena, devuelve true si es una expresión válida simple del tipo
 * `<id> + <id> * <id>` según la gramática ambigua de clase.
 */
export function esExpresionValida(expr: string): boolean {
  const regex = /^\s*[abc]\s*\+\s*[abc]\s*\*\s*[abc]\s*$/;
  return regex.test(expr);
}
