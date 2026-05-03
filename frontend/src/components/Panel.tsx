import type { ReactNode } from 'react'

type PanelProps = {
  children: ReactNode
  className?: string
  id?: string
}

export function Panel({ children, className = '', id }: PanelProps) {
  return (
    <section id={id} className={`panel ${className}`.trim()}>
      {children}
    </section>
  )
}