/**
 * Renders an inline SVG string safely.
 * If the content does not start with "<svg", renders it as plain text.
 */
export default function SvgVisual({ content, className = '' }) {
  if (!content) return null

  if (content.includes('<svg')) {
    return (
      <div
        className={className}
        dangerouslySetInnerHTML={{ __html: content }}
      />
    )
  }

  return <div className={className}>{content}</div>
}
