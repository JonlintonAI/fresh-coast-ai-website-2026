/* Editorial click events only. No conversion configuration or form changes. */
(() => {
  const events = new Set(['case_study_open', 'case_study_contact', 'case_study_pdf_download']);
  document.addEventListener('click', event => {
    const link = event.target.closest('a[data-case-event]');
    if (!link || !events.has(link.dataset.caseEvent) || typeof window.gtag !== 'function') return;
    // Queue with the existing Google tag. Never delay or prevent navigation.
    window.gtag('event', link.dataset.caseEvent, {
      case_study_id: 'stanton_company_kpi_digest',
      placement: link.dataset.casePlacement || 'navigation',
      transport_type: 'beacon'
    });
  });
})();
